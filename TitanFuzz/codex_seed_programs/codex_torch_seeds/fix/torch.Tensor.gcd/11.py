'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.gcd\ntorch.Tensor.gcd(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(2, 3, 4, 5)
other = torch.randint(10, (2, 3, 4, 5), dtype=torch.int)
_output_tensor = _input_tensor.gcd(other)
print('Input data: ', _input_tensor)
print('Other data: ', other)
print('Output data: ', _output_tensor)