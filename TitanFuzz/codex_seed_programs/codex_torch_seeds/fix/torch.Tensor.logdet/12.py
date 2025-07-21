'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logdet\ntorch.Tensor.logdet(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3, 4)
_output_tensor = torch.Tensor.logdet(_input_tensor)
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)