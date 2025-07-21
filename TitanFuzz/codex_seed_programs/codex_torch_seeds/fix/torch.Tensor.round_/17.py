'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round_\ntorch.Tensor.round_(_input_tensor)\n'
import torch
input_tensor = torch.rand(1, 3, 3)
print('input_tensor:')
print(input_tensor)
torch.Tensor.round_(input_tensor)
print('output_tensor:')
print(input_tensor)