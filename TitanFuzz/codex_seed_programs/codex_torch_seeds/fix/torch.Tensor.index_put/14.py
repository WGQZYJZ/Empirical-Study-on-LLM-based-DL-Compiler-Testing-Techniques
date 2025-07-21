'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
print('input_tensor:', input_tensor)
indices = torch.tensor([[0, 1, 2], [1, 1, 1]])
values = torch.tensor([1, 2])
output_tensor = torch.Tensor.index_put(input_tensor, indices, values, accumulate=False)
print('output_tensor:', output_tensor)