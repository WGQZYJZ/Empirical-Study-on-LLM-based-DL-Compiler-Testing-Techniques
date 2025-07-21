'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nelement\ntorch.Tensor.nelement(_input_tensor)\n'
import torch
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print('input tensor:', _input_tensor)
print('number of elements in input tensor:', _input_tensor.nelement())