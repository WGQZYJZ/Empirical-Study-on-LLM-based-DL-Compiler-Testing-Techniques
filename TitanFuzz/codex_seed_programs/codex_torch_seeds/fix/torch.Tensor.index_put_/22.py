'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put_\ntorch.Tensor.index_put_(_input_tensor, indices, values, accumulate=False)\n'
import torch
import torch
input_tensor = torch.rand(5, 3)
indices = torch.tensor([[0, 0], [4, 2]])
values = torch.tensor([1, 2])
input_tensor.index_put_(indices, values)
print('input_tensor:', input_tensor)