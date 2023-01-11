#!/bin/bash

pytest -s -v -m  "sanity" --html=Reports/reports.html testCases/    --browser chrome

