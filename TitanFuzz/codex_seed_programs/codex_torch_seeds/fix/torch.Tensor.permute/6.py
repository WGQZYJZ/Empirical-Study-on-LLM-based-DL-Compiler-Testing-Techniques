'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.permute\ntorch.Tensor.permute(_input_tensor, *dims)\n'
import torch
input_tensor = torch.randn(1, 2, 3, 4)
print('input_tensor: ', input_tensor)
permuted_tensor = input_tensor.permute(0, 2, 3, 1)
print('permuted_tensor: ', permuted_tensor)
permuted_tensor = input_tensor.permute(1, 0, 2, 3)
print('permuted_tensor: ', permuted_tensor)
permuted_tensor = input_tensor.permute(0, 3, 2, 1)
print('permuted_tensor: ', permuted_tensor)