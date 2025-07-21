'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.conj\ntorch.Tensor.conj(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.conj(_input_tensor)
print('input tensor: ', _input_tensor)
print('output tensor: ', _output_tensor)