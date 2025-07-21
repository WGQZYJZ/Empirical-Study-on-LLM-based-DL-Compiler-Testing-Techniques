'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, divisor)\n'
import torch
tensor_input = torch.randn(4, 4)
print('Input data: ', tensor_input)
tensor_output = tensor_input.remainder_(2)
print('Output data: ', tensor_output)