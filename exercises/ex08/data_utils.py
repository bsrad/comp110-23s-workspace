"""ex08 Data Wrangling."""

__author__ = "730487901"

from csv import DictReader

def read_csv_rows(filename: str) -> list[dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result

def column_values(table: list[dict[str,str]], header: str) -> list[str]:
    """Returns values in a table column under a specific header."""
    result: list[str] = []
    #step through table
    for row in table:
        result.append(row[header])
    #save every value under key "header"
    return result

def columnar(table: list[dict[str,str]]) -> dict[str,list[str]]:
    """Reformats data so that it's a dict with column headers as keys."""
    result: dict[str,list[str]] = {}
    #loop through keys of one row of table
    first_row: dict[str,str] = table[0]
    for key in first_row:
         #for rach key, make a dictionary entry with all column values
         result[key] =  column_values(table, key)
    return result

def head(table: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    return_dict: dict[str, list[str]] = {}
    for key in table:
        sub_list: list[str] = []
        data_to_get: list[str] = table[key]
        return_dict[key] = sub_list
        idx: int = 0
        x: int = 0
        if N >= len(table[key]):
            while x < len(table[key]):
                sub_list.append(data_to_get[x])
                x += 1
        else:
            while idx < N:
                sub_list.append(data_to_get[idx])
                idx += 1
    return return_dict

def select(table: dict[str, list[str]], column_names: list[str]) -> dict[str, list[str]]:
    return_dict: dict[str, list[str]] = {}
    for key in column_names:
        sub_list: list[str] = []
        data_to_get: list[str] = table[key]
        return_dict[key] = sub_list
        idx: int = 0
        while idx < len(table[key]):
            sub_list.append(data_to_get[idx])
            idx += 1
    return return_dict
    
def concat(table: dict[str, list[str]], add_table: dict[str, list[str]]) -> dict[str, list[str]]:
   result_dict: dict[str, list[str]] = {}
   for column in table:
       result_dict[column] = table[column]
   for column in add_table:
       if column in result_dict:
           for value in add_table[column]:
               result_dict[column].append(value)
       else:
           result_dict[column] = add_table[column]
   return result_dict