'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(4, 4)
indices = torch.tensor([0, 2])
values = torch.tensor([10, 20])
input_tensor.index_put_((indices, indices), values)
print(input_tensor)