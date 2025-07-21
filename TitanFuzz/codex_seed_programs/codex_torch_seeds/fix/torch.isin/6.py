'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
elements = torch.randint(0, 10, (2, 3))
test_elements = torch.randint(0, 10, (2, 3))
isin_result = torch.isin(elements, test_elements)
print('elements: ', elements)
print('test_elements: ', test_elements)
print('isin_result: ', isin_result)