'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_and_\ntorch.Tensor.logical_and_(_input_tensor, other)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.bool)
other = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.bool)
torch.Tensor.logical_and_(input_tensor, other)
print(input_tensor)
print(other)