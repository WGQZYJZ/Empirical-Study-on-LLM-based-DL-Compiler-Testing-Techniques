'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
elements = torch.tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
test_elements = torch.tensor([0, 2, 4, 6, 8])
result = torch.isin(elements, test_elements)
print(result)
print(result.dtype)