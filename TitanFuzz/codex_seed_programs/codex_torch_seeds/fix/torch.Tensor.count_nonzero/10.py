'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.randint(0, 2, (3, 4), dtype=torch.int32)
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.count_nonzero(_input_tensor, dim=None)
print('Output tensor: ', _output_tensor)