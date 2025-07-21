'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 4)
_output_tensor = torch.Tensor.sign(_input_tensor)
print('The input tensor:\n', _input_tensor)
print('The output tensor:\n', _output_tensor)