'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.type_as\ntorch.Tensor.type_as(_input_tensor, tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_input_tensor = _input_tensor.type(torch.FloatTensor)
_output_tensor = _input_tensor.type_as(_input_tensor)
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)