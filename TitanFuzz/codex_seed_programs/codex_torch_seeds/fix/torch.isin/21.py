'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isin\ntorch.isin(elements, test_elements, *, assume_unique=False, invert=False)\n'
import torch
input_tensor = torch.tensor([[0, 0, 0], [1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4]])
test_tensor = torch.tensor([[1, 1, 1], [2, 2, 2]])
isin_result = torch.isin(input_tensor, test_tensor)
print('Input tensor: ', input_tensor)
print('Test tensor: ', test_tensor)
print('Is in result: ', isin_result)