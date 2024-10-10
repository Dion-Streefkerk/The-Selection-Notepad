<template>
    <div class="container mt-4">
      <div class="card">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Edit Note</h2>
          
          <!-- Form to Edit Note -->
          <form @submit.prevent="updateNote" class="mb-4 editor-form">
            <div class="mb-3">
              <label for="title" class="form-label">Title</label>
              <input 
                type="text" 
                v-model="title" 
                class="form-control editor-title" 
                id="title" 
                placeholder="Edit title" />
            </div>
            <div class="mb-3 editor-container">
              <label for="content" class="form-label">Content</label>
              <div class="editor-wrapper">
                <div class="line-numbers">
                  <span v-for="line in lineNumbers" :key="line">{{ line }}</span>
                </div>
                <div 
                  contenteditable="true" 
                  ref="contentEditor" 
                  @input="onInputContent"
                  class="editor editor-content"
                  id="content"
                  placeholder="Edit content">
                </div>
              </div>
            </div>
            <button type="submit" class="btn btn-primary w-100">
              Update Note
            </button>
          </form>
  
          <!-- Message Display -->
          <p v-if="message" class="mt-3 alert alert-warning text-center">{{ message }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, onMounted, ref, nextTick } from 'vue';
  import api from '@/api';
  import { useRoute, useRouter } from 'vue-router';
  import hljs from 'highlight.js';
  
  export default defineComponent({
    name: 'EditNote',
    setup() {
      const route = useRoute();
      const router = useRouter();
      const noteId = route.params.noteId;
  
      // Reactive state variables
      const title = ref<string>('');
      const content = ref<string>('');
      const message = ref<string>('');
      const lineNumbers = ref<number[]>([1]);
  
      // Reference to the contenteditable element
      const contentEditor = ref<HTMLElement | null>(null);
  
      // Fetch note from API
      const fetchNote = async () => {
        try {
          const response = await api.get(`/notes/${noteId}`);
          const note = response.data;
          title.value = note.title;
          content.value = note.content;
          nextTick(() => {
            if (contentEditor.value) {
              contentEditor.value.innerText = content.value;
              updateLineNumbers();
              highlightCode();
            }
          });
        } catch (error: any) {
          message.value = 'Error fetching note';
        }
      };
  
      // Input handler for content editor
      const onInputContent = () => {
        if (contentEditor.value) {
          content.value = contentEditor.value.innerText.trim();
          updateLineNumbers();
          highlightCode();
        }
      };
  
      // Update line numbers based on content
      const updateLineNumbers = () => {
        if (contentEditor.value) {
          const lines = contentEditor.value.innerText.split('\n').length;
          lineNumbers.value = Array.from({ length: lines }, (_, i) => i + 1);
        }
      };
  
      // Highlight code blocks using highlight.js
      const highlightCode = () => {
        if (contentEditor.value) {
          contentEditor.value.querySelectorAll('code').forEach((block) => {
            hljs.highlightElement(block as HTMLElement);
          });
        }
      };
  
      // Update the note
      const updateNote = async () => {
        try {
          await api.put(`/notes/${noteId}`, {
            title: title.value,
            content: content.value,
          });
          message.value = 'Note updated successfully';
          router.push('/notes'); // Redirect to notes list after successful update
        } catch (error: any) {
          message.value = error.response?.data.error || 'An error occurred while updating the note';
        }
      };
  
      // Fetch note when component is mounted
      onMounted(() => {
        fetchNote();
      });
  
      return {
        title,
        content,
        message,
        contentEditor,
        onInputContent,
        updateNote,
        lineNumbers,
      };
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles to enhance the look */
  .card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
  }
  
  .editor-form .editor {
    background: #1e1e1e;
    color: #c9d1d9;
    padding: 10px;
    border-radius: 5px;
    font-family: 'Courier New', Courier, monospace;
    min-height: 150px;
    border: 1px solid #444;
    outline: none;
    white-space: pre-wrap;
  }
  
  .editor-container {
    position: relative;
    display: flex;
  }
  
  .line-numbers {
    user-select: none;
    padding-right: 10px;
    text-align: right;
    color: #888;
    margin-top: 10px;
  }
  
  .line-numbers span {
    display: block;
  }
  
  .editor-wrapper {
    display: flex;
    flex-direction: row;
    background-color: #1e1e1e;
    border-radius: 5px;
    padding: 10px;
  }
  
  .editor-content {
    flex-grow: 1;
    white-space: pre-wrap;
    overflow-wrap: break-word;
  }
  
  .editor-wrapper .editor-content:focus {
    outline: none;
  }
  
  .alert {
    margin-top: 20px;
    font-weight: bold;
  }
  
  .hljs {
    background: transparent; /* Ensure syntax highlighting doesn't change background */
    padding: 0;
    color: inherit;
  }
  </style>