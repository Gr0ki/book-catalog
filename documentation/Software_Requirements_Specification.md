# **Book Catalog**

## **Overview**

- The Book Catalog is a web application that allows **reading**, **writing**, **updating**, and **deleting** **books**, **genres**, and **authors**.
- It provides **HTML forms** and **REST API** to perform these actions on stored data.
- The application also offers an opportunity to **search books by published dates** in API and Forms.

## **Content**

- **[`Entities`](#entities)**
- **[`Forms`](#forms)**
    - **[`0. Home`](#0-home)**
    - **[`1. Books`](#1-books)**
      - **[`1.1 Display the list of books`](#11-display-the-list-of-books)**
      - **[`1.2 Display book details`](#12-display-book-details)**
      - **[`1.3 Add a new book`](#13-add-a-new-book)**
      - **[`1.4 Edit the book`](#14-edit-the-book)**
      - **[`1.5 Remove the book`](#15-remove-the-book)**
    - **[`2. Genres`](#2-genres)**
      - **[`2.1 Display the list of genres`](#21-display-the-list-of-genres)**
      - **[`2.2 Display genre details`](#22-display-genre-details)**
      - **[`2.3 Add a new genre`](#23-add-a-new-genre)**
      - **[`2.4 Edit the genre`](#24-edit-the-genre)**
      - **[`2.5 Remove the genre`](#25-remove-the-genre)**
    - **[`3. Authors`](#3-authors)**
      - **[`3.1 Display the list of authors`](#31-display-the-list-of-authors)**
      - **[`3.2 Display author details`](#32-display-author-details)**
      - **[`3.3 Add a new author`](#33-add-a-new-author)**
      - **[`3.4 Edit the author`](#34-edit-the-author)**
      - **[`3.5 Remove the author`](#35-remove-the-author)**
    - **[`4. API`](#4-api)**
- **[`API`](#api)**
    - **[`Endpoints`](#endpoints)**
    - **[`Reponse format`](#reponse-format)**
    - **[`Pagination`](#pagination)**
    - **[`Versioning`](#versioning)**

# **Entities**

##  **Book**

A book is an entity that has the following attributes:

    id (int)
    Title (string)
    Author
    Genre
    Publication date (date)
    Description (string)

## **Genre**

A genre is an entity that has the following attributes:

    id (int)
    Name (string)
    Description (string)

## **Author**

An author is an entity that has the following attributes:

    id (int)
    Name (string)
    Bio (string)

# **Forms**

## **0. Home**

#### *Description*

The first page of the application greets the user and provides navigation on the page.
The navigation bar is the same for all application pages except for API.

## **1. Books**

### **1.1 Display the list of books**

#### *Description*

The page is designed to list all the books and filter them by publishing date with a user-provided date range.

#### *Main scenario:*

- User selects item "Books";
- Application displays the list of the books (up to 10 items on each page);
- To see the next 10 records of the books in the database, the user needs to click the "Next" button (below the records in the pagination block) or the following number of the page the user wants to see.


#### *Filtering by date:*

- User specifies dates range in the specific input forms above data;
- User hits the refresh button to the right from dates inputs;
- The application displays the list of books with publication dates in the user-provided dates range.

<p></p>
<img src="./mockups/books/list.png" width=700>
<p></p>

The list displays the following columns:
- id - unique book number
- Title
- Author
- Genre
- Publication date

### **1.2 Display book details**

#### *Main scenario:*

- User clicks on the "Title" of the specific book from the list on the book list page;
- Application displays the user-chosen book details;

<p></p>
<img src="./mockups/books/details.png" width=700>
<p></p>

On book details page the application displays the following columns:
- id - unique book number
- Title
- Author
- Genre
- Description
- Publication date

### **1.3 Add a new book**

#### *Description*

The creation page is designed to create a record of the new book in the database.

#### *Main scenario:*

- User clicks the "Create new" button in the book list page;
- Application displays form to enter book data;
- User enters book data and presses "Submit" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is adding to database;
- If error occurs, then error message is displaying;
- If new book record is successfully added, then list of books with added records is displaying.

#### *Cancel operation scenario:*

- User clicks the "Create new" button in the book list page;
- Application displays form to enter book data;
- User may start entering the data into the form fields;
- Before pressing "Submit" button user presses “Cancel” button;
- Data doesn’t save in the database, then a list of books records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be saved to the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/books/update_or_create.png" width=700>
<p></p>

When creating a new book, the following details are entered:
- Title
- Author
- Genre
- Description
- Publication date

### **1.4 Edit the book**

#### *Description*

The edit page is designed to edit an existing book record in the database.

#### *Main scenario:*

- User clicks the "Update" button (to the right from the book he/she wants to update) on the book list/details page;
- Application displays form to enter book data;
- User enters book data he/she wants to update and presses "Submit" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then the book is updated in the database;
- If an error occurs, then the error message is displayed;
- If a new book record is successfully updated, then the list of the books with updated records is displayed.

#### *Cancel operation scenario:*

- User clicks the "Update" button (to the right from the book he/she wants to update) on the book list/details page;
- Application displays form to enter book data;
- User may start entering the data into the form fields;
- Before pressing "Submit" button user presses “Cancel” button;
- Data doesn’t update in the database, then a list of books records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be update in the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/books/update_or_create.png" width=700>
<p></p>

When editing a book, the following details are entered:
- Title
- Author
- Genre
- Description
- Publication date

### **1.5 Remove the book**

#### *Main scenario:*

- User clicks the "Delete" button (to the right from the book he/she wants to delete) on the book list/details page;
- Application displays a dialog page to confirm destroying the record for chosen book;
- User confirms deletion by pressing "Confirm" button.

#### *Cancel operation scenario:*

- User clicks the "Delete" button (to the right from the book he/she wants to delete) on the book list/details page;
- Application displays a dialog page to confirm destroying the record for chosen book;
- User presses “Cancel” button;
- Data doesn’t delete in the database, then a list of books records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be deleted from the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/books/delete.png" width=700>
<p></p>

## **2. Genres**

### **2.1 Display the list of genres**

#### *Description*

The page is designed to list all the genres.

#### *Main scenario:*

- User selects item "Genres";
- Application displays the list of the genres (up to 10 items on each page);
- To see the next 10 records of the genres in the database, the user needs to click the "Next" button (below the records in the pagination block) or the following number of the page the user wants to see.

<p></p>
<img src="./mockups/genres/list.png" width=700>
<p></p>

The list displays the following columns:

- id - unique genre number
- Name
- Description

### **2.2 Display genre details**

#### *Main scenario:*

- User clicks on the "Name" of the specific genre from the list on the genre list page;
- Application displays the user-chosen genre details;

<p></p>
<img src="./mockups/genres/details.png" width=700>
<p></p>

On genre details page the application displays the following columns:
- id - unique genre number
- Name
- Description


### **2.3 Add a new genre**

#### *Description*

The creation page is designed to create a record of the new genre in the database.

#### *Main scenario:*

- User clicks the "Create new" button in the genre list page;
- Application displays form to enter book data;
- User enters book data and presses "Submit" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is adding to database;
- If error occurs, then error message is displaying;
- If new genre record is successfully added, then list of genres with added records is displaying.

#### *Cancel operation scenario:*

- User clicks the "Create new" button in the genre list page;
- Application displays form to enter genre data;
- User may start entering the data into the form fields;
- Before pressing "Submit" button user presses “Cancel” button;
- Data doesn’t save in the database, then a list of genres records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be saved to the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/genres/update_or_create.png" width=700>
<p></p>

When creating a new genre, the following details are entered:
- Name
- Description

### **2.4 Edit the genre**

#### *Description*

The edit page is designed to edit an existing genre record in the database.

#### *Main scenario:*

- User clicks the "Update" button (to the right from the genre he/she wants to update) on the genre list/details page;
- Application displays form to enter genre data;
- User enters genre data he/she wants to update and presses "Submit" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then the genre is updated in the database;
- If an error occurs, then the error message is displayed;
- If a new genre record is successfully updated, then the list of the genres with updated records is displayed.

#### *Cancel operation scenario:*

- User clicks the "Update" button (to the right from the genre he/she wants to update) on the genre list/details page;
- Application displays form to enter genre data;
- User may start entering the data into the form fields;
- Before pressing "Submit" button user presses “Cancel” button;
- Data doesn’t update in the database, then a list of genres records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be update in the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/genres/update_or_create.png" width=700>
<p></p>

When editing a genre, the following details are entered:
- Name
- Description

### **2.5 Remove the genre**

#### *Main scenario:*

- User clicks the "Delete" button (to the right from the genre he/she wants to delete) on the genre list/details page;
- Application displays a dialog page to confirm destroying the record for chosen genre;
- User confirms deletion by pressing "Confirm" button.

#### *Cancel operation scenario:*

- User clicks the "Delete" button (to the right from the genre he/she wants to delete) on the genre list/details page;
- Application displays a dialog page to confirm destroying the record for chosen genre;
- User presses “Cancel” button;
- Data doesn’t delete in the database, then a list of genres records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be deleted from the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/genres/delete.png" width=700>
<p></p>

## **3. Authors**

### **3.1 Display the list of authors**

#### *Description*

The page is designed to list all the authors.

#### *Main scenario:*

- User selects item "Authors";
- Application displays the list of the authors (up to 10 items on each page);
- To see the next 10 records of the authors in the database, the user needs to click the "Next" button (below the records in the pagination block) or the following number of the page the user wants to see.

<p></p>
<img src="./mockups/authors/list.png" width=700>
<p></p>

The list displays the following columns:
- id - unique author number
- Name
- Bio - author's biography

### **3.2 Display author details**

#### *Main scenario:*

- User clicks on the "Title" of the specific author from the list on the author list page;
- Application displays the user-chosen author details;

<p></p>
<img src="./mockups/authors/details.png" width=700>
<p></p>

On author details page the application displays the following columns:
- id - unique author number
- Name
- Bio - author's biography

### **3.3 Add a new author**

#### *Description*

The creation page is designed to create a record of the new author in the database.

#### *Main scenario:*

- User clicks the "Create new" button in the author list page;
- Application displays form to enter book data;
- User enters book data and presses "Submit" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then record is adding to database;
- If error occurs, then error message is displaying;
- If new author record is successfully added, then list of authors with added records is displaying.

#### *Cancel operation scenario:*

- User clicks the "Create new" button in the author list page;
- Application displays form to enter author data;
- User may start entering the data into the form fields;
- Before pressing "Submit" button user presses “Cancel” button;
- Data doesn’t save in the database, then a list of authors records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be saved to the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/authors/update_or_create.png" width=700>
<p></p>

When creating a new author, the following details are entered:
- Name
- Bio - author's biography

### **3.4 Edit the author**

#### *Description*

The edit page is designed to edit an existing author record in the database.

#### *Main scenario:*

- User clicks the "Update" button (to the right from the author he/she wants to update) on the author list/details page;
- Application displays form to enter author data;
- User enters author data he/she wants to update and presses "Submit" button;
- If any data is entered incorrectly, incorrect data messages are displayed;
- If entered data is valid, then the author is updated in the database;
- If an error occurs, then the error message is displayed;
- If a new author record is successfully updated, then the list of the authors with updated records is displayed.

#### *Cancel operation scenario:*

- User clicks the "Update" button (to the right from the author he/she wants to update) on the author list/details page;
- Application displays form to enter author data;
- User may start entering the data into the form fields;
- Before pressing "Submit" button user presses “Cancel” button;
- Data doesn’t update in the database, then a list of authors records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be update in the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/authors/update_or_create.png" width=700>
<p></p>

When editing a author, the following details are entered:
- Name
- Bio - author's biography

### **3.5 Remove the author**

#### *Main scenario:*

- User clicks the "Delete" button (to the right from the author he/she wants to delete) on the author list/details page;
- Application displays a dialog page to confirm destroying the record for chosen author;
- User confirms deletion by pressing "Confirm" button.

#### *Cancel operation scenario:*

- User clicks the "Delete" button (to the right from the author he/she wants to delete) on the author list/details page;
- Application displays a dialog page to confirm destroying the record for chosen author;
- User presses “Cancel” button;
- Data doesn’t delete in the database, then a list of authors records is displayed to the user;
- If the user selects the menu item "Books”, "Genres”, "Authors", "Home" or "API", the data will not be deleted from the database, and the corresponding form with updated data will be opened.

<p></p>
<img src="./mockups/authors/delete.png" width=700>
<p></p>

# ***API***

## **Endpoints**

### **Books**

    GET /api/v1/books: Retrieve a list of all books
    GET /api/v1/books/<book_id>: Retrieve a specific book by ID
    POST /api/v1/books: Create a new book
    PUT /api/v1/books/<book_id>: Update a specific book by ID
    DELETE /api/v1/books/<book_id>: Delete a specific book by ID

Retrieve a list of books published after or before or between the given dates. (The date format should be in yyyy-mm-dd):

    GET /api/v1/books?before_date=<date>
    GET /api/v1/books?after_date=<date>
    GET /api/v1/books?after_date=<date>&before_date=<date>

### **Genres**

    GET /api/v1/genres: Retrieve a list of all genres
    GET /api/v1/genres/<genre_id>: Retrieve a specific genre by ID
    POST /api/v1/genres: Create a new genre
    PUT /api/v1/genres/<genre_id>: Update a specific genre by ID
    DELETE /api/v1/genres/<genre_id>: Delete a specific genre by ID

### **Authors**

    GET /api/v1/authors: Retrieve a list of all authors
    GET /api/v1/authors/<author_id>: Retrieve a specific author by ID
    POST /api/v1/authors: Create a new author
    PUT /api/v1/authors/<author_id>: Update a specific author by ID
    DELETE /api/v1/authors/<author_id>: Delete a specific author by ID

## **Reponse format**

The Book Catalog API returns data in JSON format. A typical response for a successful request (empty response body for 204 response code, deletion) will have the following structure:

json:

    {
      ...
    }

In case of an error, the response will have the following structure:

json for single message:

    {
      "message": "Error message"
    }

json for multiple messages:

    {
    "message": {
      "error1": [
        "message"
      ],
        "error2": [
          "message"
        ]
      }
    }

## **Pagination**

The GET /books, GET /genres and GET /authors endpoints support pagination. By default, the API returns the first 10 items. The client can specify the number of items to return using the limit query parameter, and the starting point using the offset query parameter.

## **Versioning**

The Book Catalog API uses versioning to ensure that client applications are not impacted by changes to the API. The API version is specified in the URL, e.g. /v1/books.