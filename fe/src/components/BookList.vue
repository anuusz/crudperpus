<template>
  <div class="container">
    <h1>Novel Library</h1>
    <form @submit.prevent="submitForm" class="form">
      <input v-model="currentBook.title" placeholder="Title" />
      <input v-model="currentBook.author" placeholder="Author" />
      <input v-model="currentBook.published_date" type="date" placeholder="Published Date" />
      <input v-model="currentBook.isbn" placeholder="ISBN" />
      <input v-model="currentBook.pages" placeholder="Pages" />
      <button type="submit">{{ isEditing ? 'Update Book' : 'Add Book' }}</button>
      <button v-if="isEditing" @click="cancelEdit" type="button" class="cancel">Cancel</button>
    </form>

    <table>
      <thead>
        <tr>
          <th>Title</th>
          <th>Author</th>
          <th>Published Date</th>
          <th>ISBN</th>
          <th>Pages</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="book in books" :key="book.id">
          <td>{{ book.title }}</td>
          <td>{{ book.author }}</td>
          <td>{{ book.published_date }}</td>
          <td>{{ book.isbn }}</td>
          <td>{{ book.pages }}</td>
          <td>
            <button @click="editBook(book)" class="update">Update</button>
            <button @click="deleteBook(book.id)" class="delete">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: #fff;
  padding: 20px;
}

.form {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.form input {
  margin: 5px;
  padding: 8px;
  width: 250px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.form button {
  padding: 10px 20px;
  margin-top: 10px;
  background-color: green;
  color: white;
  border-radius: 25px;
  cursor: pointer;
}

.form button:hover {
  background-color: darkgreen;
}

.form button[type="button"] {
  background-color: gray;
}

.form button[type="button"]:hover {
  background-color: darkgray;
}

table {
  width: 100%;
  max-width: 900px;
  margin-top: 20px;
  border-collapse: collapse;
  text-align: left;
  border: 1px solid #ddd;
}

th, td {
  padding: 10px;
  border: 1px solid #ddd;
}

th {
  background-color: #fff;
}

button {
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 25px;
}

.update {
  background-color: green;
}

.update:hover {
  background-color: darkgreen;
}

.delete {
  background-color: red;
}

.delete:hover {
  background-color: darkred;
}
</style>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      books: [],
      currentBook: { title: '', author: '', published_date: '', isbn: '', pages: '' },
      isEditing: false,
    };
  },
  methods: {
    fetchBooks() {
      axios.get('http://127.0.0.1:8000/api/books/').then((response) => {
        this.books = response.data;
      });
    },
    submitForm() {
      if (this.isEditing) {
        // Update book
        axios.put(`http://127.0.0.1:8000/api/books/${this.currentBook.id}/`, this.currentBook)
          .then(() => {
            this.fetchBooks();
            this.cancelEdit();
          })
          .catch((error) => {
            console.error('Error updating book:', error);
          });
      } else {
        // Add new book
        axios.post('http://127.0.0.1:8000/api/books/', this.currentBook)
          .then(() => {
            this.fetchBooks();
            this.resetForm();
          })
          .catch((error) => {
            console.error('Error adding book:', error);
          });
      }
    },
    deleteBook(id) {
      axios.delete(`http://127.0.0.1:8000/api/books/${id}/`).then(() => {
        this.fetchBooks();
      });
    },
    editBook(book) {
      this.isEditing = true;
      this.currentBook = { ...book }; 
    },
    cancelEdit() {
      this.isEditing = false;
      this.resetForm();
    },
    resetForm() {
      this.currentBook = { title: '', author: '', published_date: '', isbn: '', pages: '' };
    },
  },
  mounted() {
    this.fetchBooks();
  },
};
</script>