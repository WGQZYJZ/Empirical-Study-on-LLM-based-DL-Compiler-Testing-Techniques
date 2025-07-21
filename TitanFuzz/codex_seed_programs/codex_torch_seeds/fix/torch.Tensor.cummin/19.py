'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummin\ntorch.Tensor.cummin(_input_tensor, dim)\n'
import torch
_input_tensor = torch.tensor([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print('Input tensor:')
print(_input_tensor)
cummin_result = torch.Tensor.cummin(_input_tensor, dim=1)
print('Output tensor:')
print(cummin_result)