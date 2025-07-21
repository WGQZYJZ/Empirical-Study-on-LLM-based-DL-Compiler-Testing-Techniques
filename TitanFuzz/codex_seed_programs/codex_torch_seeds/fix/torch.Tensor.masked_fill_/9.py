'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randn(2, 3)
mask = torch.ByteTensor([[0, 0, 1], [0, 1, 0]])
value = 10
print(input_tensor)
print(mask)
torch.Tensor.masked_fill_(input_tensor, mask, value)
print(input_tensor)