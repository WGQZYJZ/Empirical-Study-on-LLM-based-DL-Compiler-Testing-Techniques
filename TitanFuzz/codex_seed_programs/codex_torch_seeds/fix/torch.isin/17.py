'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
elements = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_elements = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
output = torch.isin(elements, test_elements)
print('input elements: ', elements)
print('test_elements: ', test_elements)
print('output: ', output)
output = torch.isin(elements, test_elements, invert=True)
print('input elements: ', elements)
print('test_elements: ', test_elements)
print('output: ', output)