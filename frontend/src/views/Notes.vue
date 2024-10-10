<template>
    <div class="container mt-4">
      <div class="card">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Notes</h2>
  
          <!-- Form to Add Notes -->
          <form @submit.prevent="submitNote" class="mb-4 editor-form">
            <div class="form-section mb-4">
              <label for="title" class="form-label">Title</label>
              <input
                type="text"
                v-model.trim="title"
                class="form-control editor-title"
                id="title"
                placeholder="Enter title" />
            </div>
            <div class="form-section mb-4">
              <label for="content" class="form-label">Content</label>
              <pre
                ref="contentEditor"
                @input="onInputContent"
                class="editor editor-content"
                id="content"
                contenteditable="true"
                placeholder="Enter content"></pre>
            </div>
            <button type="submit" class="btn btn-primary w-100">Add Note</button>
          </form>
  
          <!-- List of Notes -->
          <div v-if="notes.length" class="note-list">
            <div v-for="note in notes" :key="note.id" class="note-item">
              <h5 class="note-title">{{ note.title }}</h5>
              <pre class="note-content">
                <code class="hljs">
                  {{ note.content }}
                </code>
              </pre>
              <div class="note-actions">
                <button @click="copyToClipboard(note.content)" class="btn btn-sm btn-outline-success me-2">Copy Snippet</button>
                <button @click="goToEdit(note.id)" class="btn btn-sm btn-outline-secondary me-2">Edit</button>
                <button @click="deleteNote(note.id)" class="btn btn-sm btn-outline-danger">Delete</button>
              </div>
            </div>
          </div>
          <div v-else class="alert alert-info text-center">No notes available. Add a note to get started.</div>
  
          <!-- Message Display -->
          <p v-if="message" class="mt-3 alert alert-warning text-center">{{ message }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, onMounted, ref, nextTick } from 'vue';
  import api from '@/api';
  import { useRouter } from 'vue-router';
  import hljs from 'highlight.js';
  
  interface Note {
    id: number;
    title: string;
    content: string;
    user_id: number;
  }
  
  export default defineComponent({
    name: 'Notes',
    setup() {
      const router = useRouter();
  
      // Reactive state variables with explicit types
      const notes = ref<Note[]>([]);
      const title = ref<string>('');
      const content = ref<string>('');
      const message = ref<string>('');
  
      // Reference to the contenteditable element
      const contentEditor = ref<HTMLElement | null>(null);
  
      // Fetch notes from API
      const fetchNotes = async () => {
        try {
          const response = await api.get('/notes');
          notes.value = response.data;
          nextTick(() => {
            highlightCode();
          });
        } catch (error: any) {
          message.value = 'Error fetching notes';
        }
      };
  
      // Highlight code blocks using highlight.js
      const highlightCode = () => {
        const blocks = document.querySelectorAll('pre code');
        blocks.forEach((block) => {
          hljs.highlightElement(block as HTMLElement);
        });
      };
  
      // Input handler for content editor
      const onInputContent = () => {
        if (contentEditor.value) {
          content.value = contentEditor.value.innerText.replace(/^\s+/, '').trim();
        }
      };
  
      // Submit new note
      const submitNote = async () => {
        try {
          const response = await api.post('/notes', {
            title: title.value,
            content: content.value,
            user_id: 1, // Replace with actual user_id (typically from token)
          });
          message.value = response.data.message;
          resetForm();
          fetchNotes(); // Refresh notes after creating
        } catch (error: any) {
          message.value = error.response?.data.error || 'An error occurred while creating the note';
        }
        nextTick(() => {
          highlightCode(); // Highlight new note after it's added
        });
      };
  
      // Navigate to EditNote view
      const goToEdit = (noteId: number) => {
        router.push({ name: 'EditNote', params: { noteId } });
      };
  
      // Delete a note
      const deleteNote = async (noteId: number) => {
        try {
          const response = await api.delete(`/notes/${noteId}`);
          message.value = response.data.message;
          fetchNotes(); // Refresh notes after deletion
        } catch (error: any) {
          message.value = 'Error deleting note';
        }
      };
  
      // Copy note content to clipboard
      const copyToClipboard = (content: string) => {
        navigator.clipboard.writeText(content).then(
          () => {
            message.value = 'Snippet copied to clipboard';
          },
          () => {
            message.value = 'Failed to copy snippet to clipboard';
          }
        );
      };
  
      // Reset form to initial state
      const resetForm = () => {
        title.value = '';
        content.value = '';
        if (contentEditor.value) contentEditor.value.innerText = '';
      };
  
      // Fetch notes when the component is mounted
      onMounted(() => {
        fetchNotes();
      });
  
      return {
        title,
        content,
        notes,
        message,
        submitNote,
        goToEdit,
        deleteNote,
        copyToClipboard,
        contentEditor,
        onInputContent,
      };
    },
  });
  </script>
  
  <style scoped>
  /* Custom styles to enhance the appearance */
  .card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
  }
  
  .form-section {
    padding-bottom: 15px;
    border-bottom: 1px solid #ccc;
    margin-bottom: 15px;
  }
  
  .editor-form .editor {
    background: #1e1e1e;
    color: #c9d1d9;
    padding: 20px;
    border-radius: 5px;
    font-family: 'Courier New', Courier, monospace;
    min-height: 150px;
    border: 1px solid #444;
    outline: none;
    white-space: pre-wrap;
  }
  
  .editor-wrapper {
    display: flex;
    flex-direction: column;
    background-color: #2e2e2e;
    border-radius: 5px;
    padding: 10px;
  }
  
  .note-list {
    margin-top: 20px;
  }
  
  .note-item {
    margin-bottom: 20px;
    padding: 15px;
    background-color: #1e1e1e;
    color: #c9d1d9;
    border-radius: 5px;
  }
  
  .note-title {
    font-size: 1.25rem;
    font-weight: bold;
    margin-bottom: 10px;
  }
  
  .note-content {
    background: #282c34;
    padding: 10px;
    margin: 0;
    overflow: auto;
    white-space: pre-wrap;
    font-family: 'Courier New', Courier, monospace;
    color: #c9d1d9;
    border: 1px solid #444;
    border-radius: 5px;
  }
  
  .note-actions {
    margin-top: 10px;
  }
  
  .btn {
    transition: background-color 0.2s, color 0.2s;
  }
  
  .btn:hover {
    opacity: 0.9;
  }
  
  .alert {
    margin-top: 20px;
    font-weight: bold;
  }
</style>