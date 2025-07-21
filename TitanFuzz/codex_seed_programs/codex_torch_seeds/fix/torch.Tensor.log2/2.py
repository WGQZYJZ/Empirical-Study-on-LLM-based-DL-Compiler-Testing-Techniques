'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.log2\ntorch.Tensor.log2(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3, 224, 224)
_output_tensor = _input_tensor.log2()
print('Input tensor: ', _input_tensor)
print('Output tensor: ', _output_tensor)