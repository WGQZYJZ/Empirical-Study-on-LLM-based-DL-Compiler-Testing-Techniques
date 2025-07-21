'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose_\ntorch.Tensor.transpose_(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(3, 2), dtype=torch.int32)
print('input_tensor: ', input_tensor)
torch.Tensor.transpose_(input_tensor, 0, 1)
print('transposed input_tensor: ', input_tensor)