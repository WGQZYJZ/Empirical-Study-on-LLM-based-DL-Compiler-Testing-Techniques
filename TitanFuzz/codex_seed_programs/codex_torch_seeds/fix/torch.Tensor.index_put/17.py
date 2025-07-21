'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.rand(4, 4, 4)
indices = torch.tensor([[1, 2, 3], [0, 1, 2], [0, 1, 2], [1, 2, 3]])
values = torch.tensor([1, 2, 3, 4])
output_tensor = torch.Tensor.index_put(input_tensor, indices, values, accumulate=False)
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)