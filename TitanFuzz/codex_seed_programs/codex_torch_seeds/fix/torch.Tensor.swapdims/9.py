'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.swapdims\ntorch.Tensor.swapdims(_input_tensor, dim0, dim1)\n'
import torch
_input_tensor = torch.rand(3, 4, 5)
_output_tensor = _input_tensor.swapdims(0, 1)
print('The input tensor is: ', _input_tensor)
print('The output tensor is: ', _output_tensor)