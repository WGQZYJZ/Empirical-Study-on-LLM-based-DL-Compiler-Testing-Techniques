'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tanh\ntorch.Tensor.tanh(_input_tensor)\n'
import torch
_input_tensor = torch.randn(1, 3)
print('_input_tensor: ', _input_tensor)
_output_tensor = torch.Tensor.tanh(_input_tensor)
print('_output_tensor: ', _output_tensor)