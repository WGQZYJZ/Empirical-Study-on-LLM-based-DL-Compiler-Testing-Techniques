'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5])
test_elements = torch.tensor([1, 3, 5])
isin_result = torch.isin(input_data, test_elements)
print('Isin result: ', isin_result)