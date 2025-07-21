'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_put\ntorch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor: ', input_tensor)
indices = torch.tensor([[0, 0], [1, 2]])
values = torch.tensor([10, 20])
input_tensor.index_put((indices,), values, accumulate=False)
print('output_tensor: ', input_tensor)