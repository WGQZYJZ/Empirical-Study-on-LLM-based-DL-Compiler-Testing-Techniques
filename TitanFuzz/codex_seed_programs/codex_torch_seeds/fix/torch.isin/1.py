'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
input_data = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=torch.float32)
print(torch.isin(input_data, torch.tensor(5)))
print(torch.isin(input_data, torch.tensor(5), invert=True))
print(torch.isin(input_data, torch.tensor(5), assume_unique=True))
print(torch.isin(input_data, torch.tensor(5), assume_unique=True, invert=True))