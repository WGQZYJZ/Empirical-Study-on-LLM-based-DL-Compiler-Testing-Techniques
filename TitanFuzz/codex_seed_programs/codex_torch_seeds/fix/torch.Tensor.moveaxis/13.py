'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.moveaxis\ntorch.Tensor.moveaxis(_input_tensor, source, destination)\n'
import torch
_input_tensor = torch.randn(3, 4, 5)
_output_tensor = torch.Tensor.moveaxis(_input_tensor, 0, 2)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)