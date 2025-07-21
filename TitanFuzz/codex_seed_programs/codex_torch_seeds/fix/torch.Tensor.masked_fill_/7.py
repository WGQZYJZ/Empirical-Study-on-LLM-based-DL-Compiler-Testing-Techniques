'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.masked_fill_\ntorch.Tensor.masked_fill_(_input_tensor, mask, value\n'
import torch
input_tensor = torch.randn(3, 4)
mask = torch.randint(0, 2, (3, 4), dtype=torch.bool)
value = torch.rand(1)
torch.Tensor.masked_fill_(input_tensor, mask, value)
print(input_tensor)