from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DateField,
    SelectField,
    SubmitField,
    TextAreaField,
    PasswordField,
)
from wtforms.ext.sqlalchemy.fields import (
    QuerySelectField,
    QuerySelectMultipleField,
)
from wtforms.validators import DataRequired, Length
from books_app.models import Audience, Book, Author, Genre


class BookForm(FlaskForm):
    """Form to create a book."""

    title = StringField(
        "Book Title", validators=[DataRequired(), Length(min=3, max=80)]
    )
    publish_date = DateField("Date Published")
    author = QuerySelectField(
        "Author", query_factory=lambda: Author.query, allow_blank=False
    )
    audience = SelectField("Audience", choices=Audience.choices())
    genres = QuerySelectMultipleField(
        "Genres", query_factory=lambda: Genre.query
    )
    submit = SubmitField("Submit")


class AuthorForm(FlaskForm):
    """Form to create an author."""

    name = StringField(
        "Author Name", validators=[DataRequired(), Length(min=4, max=80)]
    )
    biography = TextAreaField(
        "Author Biography",
        validators=[DataRequired(), Length(min=5, max=200)],
    )
    submit = SubmitField("Submit")

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.


class GenreForm(FlaskForm):
    """Form to create a genre."""

    # - the genre's name (e.g. fiction, non-fiction, etc)
    name = StringField(
        "Genre Name", validators=[DataRequired(), Length(min=3, max=80)]
    )
    submit = SubmitField("Submit")


class UserForm(FlaskForm):
    """Form to create a user."""

    # The user's name
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3, max=15)]
    )
    favorite_books = StringField(
        "Add a Favorite Book",
        validators=[DataRequired(), Length(min=3, max=30)],
    )
    # password
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=8, max=12)],
    )
    submit = SubmitField("Submit")
