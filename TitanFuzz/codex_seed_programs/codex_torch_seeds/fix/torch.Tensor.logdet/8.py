'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
'\nTask 2: Generate input data\n'
_input_tensor = torch.randn(3, 3, dtype=torch.float32)
'\nTask 3: Call the API torch.Tensor.logdet\n'
_output_tensor = _input_tensor.logdet()
print('input tensor:', _input_tensor)
print('output tensor:', _output_tensor)