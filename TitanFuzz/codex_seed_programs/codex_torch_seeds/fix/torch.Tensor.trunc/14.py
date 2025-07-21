'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.trunc\ntorch.Tensor.trunc(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 2, 3, 4)
print('Input: ', _input_tensor)
_output_tensor = _input_tensor.trunc()
print('Output: ', _output_tensor)