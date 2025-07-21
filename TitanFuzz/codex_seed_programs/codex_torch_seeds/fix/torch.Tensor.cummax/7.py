'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor:')
print(input_tensor)
cummax_tensor = torch.Tensor.cummax(input_tensor, dim=0)
print('Cummax tensor:')
print(cummax_tensor)