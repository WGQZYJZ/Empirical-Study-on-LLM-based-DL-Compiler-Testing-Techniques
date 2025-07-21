'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.values\ntorch.Tensor.values(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = _input_tensor.values()
print('The input tensor is: ', _input_tensor)
print('The output tensor is: ', _output_tensor)