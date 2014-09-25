#clean_my_dataset: Json reading and writing

Introduces: json, split, join, list.

Author(s): @c24b.

## Instructions

You have a velib.json file in your directory that contains a list of every velib stations in Ile de France stored as dictionnaries.
Your program will have to read the file and write a new file with the cleaned dataset called: `solution.json`.

The clean file will contain a list of dictionnary with new keys:
* 'zip_code'
* 'city' 
and udpated keys:
* 'name' that should'nt contain any number of station
* 'address' without any zip_code or city name.

You will have to write the produces dataset into a new clean json file. 

## Advice

To read and write a json file take a look at the 'json' module.
You can solve this problem using split() and join() function.

## Example

The final datasets solution_velib.json will be stored in a single line (no identation is required)
and no need to respect the order of the values, such as:
```python
[{"number": 31705,
zip_code": "93170",
name": "CHAMPEAUX (BAGNOLET)",
longitude": 2.416170724425901,
address": "RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE)",
city": "BAGNOLET",
latitude": 48.8645278209514},
{...},
{...},
]
```



## References
 - [json](☛)
 - [json](if(comparisons))
 - [json](https://docs.python.org/3/tutorial/controlflow.html#if-statements)
 - [split](https://docs.python.org/3/library/stdtypes.html#str.split)
 - [join](https://docs.python.org/3/library/stdtypes.html#str.join)
 - [list](https://docs.python.org/3/tutorial/introduction.html#lists)
