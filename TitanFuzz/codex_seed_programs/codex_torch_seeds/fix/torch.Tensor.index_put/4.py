'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(3, 3)
indices = torch.tensor([[0, 1], [1, 2]])
values = torch.tensor([3, 4])
print('input_tensor:', input_tensor)
print('indices:', indices)
print('values:', values)
input_tensor.index_put(indices, values, accumulate=False)
print('After index_put:', input_tensor)