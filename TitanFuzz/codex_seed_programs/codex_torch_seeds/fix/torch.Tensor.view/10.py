'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
_input_tensor = torch.randn(3, 5)
_output_tensor = _input_tensor.view(15)
print('_input_tensor: ', _input_tensor)
print('_output_tensor: ', _output_tensor)