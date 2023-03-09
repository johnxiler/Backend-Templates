<?php
// Connect to the database
$host = 'localhost';
$username = 'root';
$password = '';
$dbname = 'book_db';
$conn = new mysqli($host, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Retrieve the list of books from the database
// $sql = "SELECT title, author, year FROM books";
// $result = $conn->query($sql);
// $books = array();
// if ($result->num_rows > 0) {
//     while ($row = $result->fetch_assoc()) {
//         $books[] = $row;
//     }
// }
// Retrieve the list of books from the database using a prepared statement
if (isset($_GET['search'])) {
$stmt = $conn->prepare("SELECT `id`, `title`, 
                                `author`, `year`, `average_rating`, 
                                `isbn`, `isbn13`, `language_code`, 
                                `num_pages`, `ratings_count`, 
                                `text_reviews_count`, `publication_date`, 
                                `publisher` FROM books WHERE title LIKE ? OR author LIKE ?");
$search = '%' . htmlspecialchars($_GET['search']) . '%'; // Sanitize user input to prevent XSS attacks
$stmt->bind_param("ss", $search, $search);
$stmt->execute();
$result = $stmt->get_result();
$books = array();
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $books[] = $row;
    }
}
}
// Set the content type to JSON
//header('Content-Type: application/json'); //to treat as json file rendered in the website.

// Return the list of books as JSON
// echo json_encode($books);
?>

<!DOCTYPE html>
<html>
  <head>
    <title>Fetch API Example</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <h1>Books</h1>
    <form method="get">
      <input type="text" name="search" placeholder="Search for a book...">
      <button type="submit">Search</button>
    </form>
    <table id="book-list">
      <thead>
        <tr>
          <th>Title</th>
          <th>Author</th>
          <th>Year</th>
          <th>average_rating</th>
          <th>isbn</th>
          <th>isbn13</th>
          <th>language_code</th> 
          <th>num_pages</th>
          <th>ratings_count</th> 
          <th>text_reviews_count</th>
          <th>publication_date</th> 
          <th>publisher</th>
        </tr>
      </thead>
      <tbody>
      <?php foreach ($books as $book): ?>
          <tr>
            <td><?= htmlspecialchars($book['title']) ?></td> <!-- Sanitize output to prevent XSS attacks -->
            <td><?= htmlspecialchars($book['author']) ?></td>
            <td><?= $book['year'] ?></td>
          </tr>
        <?php endforeach; ?>
      </tbody>
    </table>

    <script>
      fetch('<?= $_SERVER['PHP_SELF'] ?>')
        .then(response => response.json())
        .then(data => {
          const bookList = document.getElementById('book-list');
          data.forEach(book => {
            const li = document.createElement('li');
            li.textContent = `${book.title} by ${book.author} (${book.year})`;
            bookList.appendChild(li);
          });
        })
        .catch(error => console.error(error));
    </script>
  </body>
</html>