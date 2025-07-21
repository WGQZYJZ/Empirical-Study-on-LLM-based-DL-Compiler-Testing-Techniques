'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.rand(5, 5)
indices = torch.tensor([[0, 1], [1, 2]])
values = torch.tensor([[1, 2], [3, 4]])
output_tensor = torch.Tensor.index_put_(input_tensor, indices, values, accumulate=False)
print(output_tensor)