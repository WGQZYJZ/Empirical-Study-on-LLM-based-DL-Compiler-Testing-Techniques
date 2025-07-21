'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
input = torch.tensor([[1, 2], [3, 4]])
test_elements = torch.tensor([1, 2, 4])
result = torch.isin(input, test_elements)
print(result)