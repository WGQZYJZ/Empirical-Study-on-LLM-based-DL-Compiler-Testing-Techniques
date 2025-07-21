'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.type_as(_input_tensor, torch.FloatTensor)
print('Output tensor: ', _output_tensor)