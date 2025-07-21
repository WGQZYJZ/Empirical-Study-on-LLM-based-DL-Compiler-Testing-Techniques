'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.vsplit\ntorch.Tensor.vsplit(_input_tensor, split_size_or_sections)\n'
import torch
_input_tensor = torch.randint(0, 10, (4, 4))
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.vsplit(_input_tensor, 2)
print('Output tensor: ', _output_tensor)