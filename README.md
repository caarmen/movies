# Movies database application

The purpose of this project is to explore some query optimizations for different types of database relationships, comparing Django and Flask/SQLAlchemy.

## Setup

Create separate virtual environments for the django and flask subprojects.

For each of them:
* install dependencies with `pip install -r requirements/dev.txt`.
* Prepare the database with `scripts/prepare_db.sh`.
* Import the test data with `scripts/import_data.sh`.
* Run the server with `scripts/run_server.sh`.

## Pages

The following pages are available.

<table>
  <thead>
    <tr>
      <th>Page</th>
      <th>Relationship</th>
      <th>Scenario</th>
      <th>Django url</th>
      <th>Flask url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">Movies and finance</td>
      <td rowspan="2">One-to-one</td>
      <td>N+1 problem</td>
      <td><a href="http://localhost:8000/onetoone/nplus1/">http://localhost:8000/onetoone/nplus1/</a></td>
      <td><a href="http://localhost:5000/onetoone/sync/nplus1">http://localhost:5000/onetoone/sync/nplus1</a></td>
    </tr>
    <tr>
      <td>Fixed</td>
      <td><a href="http://localhost:8000/onetoone/optim/">http://localhost:8000/onetoone/optim/</a></td>
      <td><a href="http://localhost:5000/onetoone/sync/optim">http://localhost:5000/onetoone/sync/optim</a></td>
    </tr>
    <tr>
      <td rowspan="2">Movies and studios</td>
      <td rowspan="2">Many-to-one</td>
      <td>N+1 problem</td>
      <td><a href="http://localhost:8000/manytoone/nplus1/">http://localhost:8000/manytoone/nplus1/</a></td>
      <td><a href="http://localhost:5000/manytoone/sync/nplus1">http://localhost:5000/manytoone/sync/nplus1</a></td>
    </tr>
    <tr>
      <td>Fixed</td>
      <td><a href="http://localhost:8000/manytoone/optim/">http://localhost:8000/manytoone/optim/</a></td>
      <td><a href="http://localhost:5000/manytoone/sync/optim">http://localhost:5000/manytoone/sync/optim</a></td>
    </tr>
    <tr>
      <td rowspan="2">Movies and actors</td>
      <td rowspan="2">Many-to-many</td>
      <td>N+1 problem</td>
      <td><a href="http://localhost:8000/manytomany/nplus1/">http://localhost:8000/manytomany/nplus1/</a></td>
      <td><a href="http://localhost:5000/manytomany/sync/nplus1">http://localhost:5000/manytomany/sync/nplus1</a></td>
    </tr>
    <tr>
      <td>Fixed</td>
      <td><a href="http://localhost:8000/manytomany/optim/">http://localhost:8000/manytomany/optim/</a></td>
      <td><a href="http://localhost:5000/manytomany/sync/optim">http://localhost:5000/manytomany/sync/optim</a></td>
    </tr>
    <tr>
      <td rowspan="2">Full data</td>
      <td rowspan="2">Multiple</td>
      <td>N+1 problem</td>
      <td><a href="http://localhost:8000/full/nplus1/">http://localhost:8000/full/nplus1/</a></td>
      <td><a href="http://localhost:5000/full/sync/nplus1">http://localhost:5000/full/sync/nplus1</a></td>
    </tr>
    <tr>
      <td>Fixed</td>
      <td><a href="http://localhost:8000/full/optim/">http://localhost:8000/full/optim/</a></td>
      <td><a href="http://localhost:5000/full/sync/optim">http://localhost:5000/full/sync/optim</a></td>
    </tr>
  </tbody>
</table>

## Tests

Tests can be run with `scripts/run_tests.sh`, in each project.

