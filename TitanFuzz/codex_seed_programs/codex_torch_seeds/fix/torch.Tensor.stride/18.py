'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.stride\ntorch.Tensor.stride(_input_tensor, dim)\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
print('Input Tensor: ', _input_tensor)
print('Tensor.stride(tensor, dim): ', torch.Tensor.stride(_input_tensor, 2))
print('Tensor.stride(tensor, dim): ', torch.Tensor.stride(_input_tensor, 1))
print('Tensor.stride(tensor, dim): ', torch.Tensor.stride(_input_tensor, 0))