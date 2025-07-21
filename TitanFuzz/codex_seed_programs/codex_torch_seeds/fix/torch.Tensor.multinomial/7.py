'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multinomial\ntorch.Tensor.multinomial(_input_tensor, num_samples, replacement=False, *, generator=None)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = torch.Tensor.multinomial(_input_tensor, 2, replacement=False)
print('Input tensor:', _input_tensor)
print('Output tensor:', _output_tensor)
_output_tensor_2 = torch.Tensor.multinomial(_input_tensor, 2, replacement=True)
print('Output tensor 2:', _output_tensor_2)
'\nTask 4: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(input, dim, *, dtype=None)\n'
_input_tensor_2 = torch.randn(2, 3)
_output_tensor_3 = torch.Tensor.cumsum(_input_tensor_2, dim=1)