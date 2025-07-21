'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.isreal\ntorch.Tensor.isreal(_input_tensor)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output = torch.Tensor.isreal(_input_tensor)
print('Output: ', _output)
print('Input: ', _input_tensor)