'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.ones(3, 3)
mask = torch.tensor([[0, 0, 1], [0, 1, 1], [1, 1, 1]])
value = 3
torch.Tensor.masked_fill_(input_tensor, mask, value)
print(input_tensor)