'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
elements = torch.tensor([1, 2, 3, 4, 5])
test_elements = torch.tensor([1, 3, 5])
res = torch.isin(elements, test_elements)
print(res)
res = torch.isin(elements, test_elements, invert=True)
print(res)