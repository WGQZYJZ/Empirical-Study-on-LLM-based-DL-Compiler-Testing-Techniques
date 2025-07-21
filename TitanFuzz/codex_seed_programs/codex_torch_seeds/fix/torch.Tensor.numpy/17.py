'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.numpy\ntorch.Tensor.numpy(_input_tensor)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input data: ', _input_tensor)
_output_numpy = _input_tensor.numpy()
print('Output data: ', _output_numpy)