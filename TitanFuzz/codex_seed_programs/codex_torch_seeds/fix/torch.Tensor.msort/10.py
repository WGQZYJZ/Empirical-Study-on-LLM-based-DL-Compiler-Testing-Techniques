'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.msort\ntorch.Tensor.msort(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 5)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.msort(_input_tensor)
print('Output tensor: ', _output_tensor)