# Architecture

This repository is a sanitized public portfolio implementation of a spreadsheet-driven browser automation pattern.

## Flow

~~~text
XLSX input
   |
   v
openpyxl reader
   |
   v
field mapping + required-field validation
   |
   v
Playwright page adapter
   |
   v
stable data-testid selectors
   |
   v
submit + success verification
   |
   v
structured logging / failure count
~~~

## Engineering decisions

- Public tests use synthetic spreadsheet and HTML fixtures.
- Browser selectors are isolated in form_filler.py.
- Required-field validation occurs before browser interaction.
- Each record is processed independently.
- The repository contains no production credentials, PHI, or private client data.
- Real integrations should use approved access and organization-specific data-handling controls.
