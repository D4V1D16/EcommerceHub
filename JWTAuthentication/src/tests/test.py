from utils.DBPushQuery import pushQuery
from database.dbConnnection import get_Connection
from psycopg2 import extras
# The function executes a query with a tuple containing NULL values and returns NULL values in the result.
def test_query_with_null_values(self, mocker):
    # Mock the get_Connection function
    mock_get_connection = mocker.patch('utils.DBPushQuery.get_Connection')
    # Mock the cursor and execute methods
    mock_cursor = mocker.Mock()
    mock_cursor.fetchone.return_value = None
    mock_conn = mocker.Mock()
    mock_conn.cursor.return_value = mock_cursor
    mock_get_connection.return_value = mock_conn

    # Define the query and tuple
    query = "SELECT * FROM users WHERE id = %s"
    queryTuple = (None,)

    # Call the pushQuery function
    result = pushQuery(query, queryTuple)

    # Assert that the get_Connection function was called
    mock_get_connection.assert_called_once()

    # Assert that the cursor method was called on the connection object
    mock_conn.cursor.assert_called_once_with(cursor_factory=extras.RealDictCursor)

    # Assert that the execute method was called on the cursor object with the correct arguments
    mock_cursor.execute.assert_called_once_with(query, queryTuple)

    # Assert that the fetchone method was called on the cursor object
    mock_cursor.fetchone.assert_called_once()

    # Assert that the commit method was called on the connection object
    mock_conn.commit.assert_called_once()

    # Assert that the close method was called on the cursor object
    mock_cursor.close.assert_called_once()

    # Assert that the close method was called on the connection object
    mock_conn.close.assert_called_once()

    # Assert the result is as expected
    assert result == None