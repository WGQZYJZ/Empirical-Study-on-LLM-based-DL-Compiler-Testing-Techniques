'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.bool)
other = torch.randint(low=0, high=2, size=(5, 5), dtype=torch.bool)
print('input_tensor:', input_tensor)
print('other:', other)
torch.Tensor.logical_xor_(input_tensor, other)
print('result:', input_tensor)