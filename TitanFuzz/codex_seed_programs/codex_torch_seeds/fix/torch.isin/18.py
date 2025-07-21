'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
import torch
elements = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
test_elements = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
result = torch.isin(elements, test_elements, assume_unique=False, invert=False)
print('result: ', result)