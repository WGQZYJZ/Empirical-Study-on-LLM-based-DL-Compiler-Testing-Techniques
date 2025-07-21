'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(5, 3)
print('Input tensor:')
print(input_tensor)
torch.Tensor.fill_(input_tensor, 0)
print('After fill_:')
print(input_tensor)