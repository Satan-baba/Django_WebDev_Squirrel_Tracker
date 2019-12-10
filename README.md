# Squirrel Tracker

This is a squirrel tracking app that allows you to add and edit sightings. Moreover, it also shows a map with all the sightings and displyas basic stats about the sightings.

## Usage

On the homepage, the user can either view a list of all sigthings or view the map that plots all squirrel locations.

The map shows about 1000 squirrels in central park.

The link to edit or add will lead to the index page for the app called sightings. This shows a table which lists down the details of all the sightings in central park. The 'unique_squirrel_id' column id is clickable and can be used to edit/update/change that particular entry in the table.

In addition, there is a link to add new entries on the sightings index page. This leads to a form to create a new row in the list. 

If there is an edit in the latitude/longitude of the sighting, it is directly reflected in the map
If there is an addtion to the data and a new row is added, a new marker could be immediately seen on the map

## Importing and exporting data

to export all the data in csv format:

```bash
python manage.py export_squirrel_data /path/to/file.csv
```
file.csv will contain all the columns from the database

To import all data in database from a csv file:

```bash
python manage.py import squirrel_data /path/to/file.csv
```
This command takes in data from a csv file and puts it in the database
