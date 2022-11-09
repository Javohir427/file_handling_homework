def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list = []
    for i in data.split(','):
        list.append(int(i))
    return list
f = open('txt_file/data01.txt').read()
data=f

print(data)

# Read data from file