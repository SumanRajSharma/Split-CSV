# Split CSV

<!--- These are examples. See https://shields.io for others or to customize this set of shields. You might want to include dependencies, project status and licence info here --->
![GitHub repo size](https://img.shields.io/github/repo-size/sumanrajsharma/splitCSV)
![GitHub contributors](https://img.shields.io/github/contributors/sumanrajsharma/splitCSV)
![GitHub stars](https://img.shields.io/github/stars/sumanrajsharma/splitCSV?style=social)
![GitHub forks](https://img.shields.io/github/forks/sumanrajsharma/splitCSV?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/sumanrajsharma?style=social)

splitCSV.py is a `<python script>` that basically allows `<Data Analysts>` to split large CSVs based on provided row size. 

Function: main is a method that splits the xlxs file to multiple CSVs based on provided row size.
Variables: 
1. <filename> - filepath/name of a Excel file. Eg: '~/Desktop/test.xlsx' Or if file is in same path as this script simply 'test.xlsx'
2. <rowsize> - size of a row you want to split the Excel file to create multiple CSVs.  
3. <output_file_prefix> - output file prefix. Eg. If you provide 'result' then file name will be result_1.csv, result_2.csv ... 
    
Steps:
1. Load Excel file and create a dataframe using python library pandas
2. Split the dataframe to list/array of dataframes based on the row size you provided
3. Loop through the list to create multiple CSVs. 
    
All the CSVs are saved inside Output folder.

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed the latest version of `<coding_language/dependency/requirement_1>`
* You have a `<Windows/Linux/Mac>` machine. State which OS is supported/which is not.
* You have read `<guide/link/documentation_related_to_project>`.

## Installing <project_name>

To install <project_name>, follow these steps:

Linux and macOS:
```
<install_command>
```

Windows:
```
<install_command>
```
## Using <project_name>

To use <project_name>, follow these steps:

```
<usage_example>
```

Add run commands and examples you think users will find useful. Provide an options reference for bonus points!

## Contributing to <project_name>
<!--- If your README is long or you have some specific process or steps you want contributors to follow, consider creating a separate CONTRIBUTING.md file--->
To contribute to <project_name>, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

* [@SumanRajSharma](https://github.com/SumanRajSharma) 📖

You might want to consider using something like the [All Contributors](https://github.com/all-contributors/all-contributors) specification and its [emoji key](https://allcontributors.org/docs/en/emoji-key).

## Contact

If you want to contact me you can reach me at <sumanrajsharma2014@gmail.com>.

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [<license_name>](<link>).
