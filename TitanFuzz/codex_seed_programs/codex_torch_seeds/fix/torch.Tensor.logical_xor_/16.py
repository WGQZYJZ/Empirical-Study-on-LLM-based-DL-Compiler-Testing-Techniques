'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logical_xor_\ntorch.Tensor.logical_xor_(_input_tensor, other)\n'
import torch
input_tensor = torch.Tensor([[True, False, True], [False, True, False]])
other = torch.Tensor([[True, True, False], [False, False, True]])
result = input_tensor.logical_xor_(other)
print('Result: ', result)