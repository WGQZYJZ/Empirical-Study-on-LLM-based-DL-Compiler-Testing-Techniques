'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flip\ntorch.Tensor.flip(_input_tensor, dims)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
print('\nInput tensor:\n', _input_tensor)
_output_tensor = torch.Tensor.flip(_input_tensor, dims=[0, 2])
print('\nOutput tensor:\n', _output_tensor)