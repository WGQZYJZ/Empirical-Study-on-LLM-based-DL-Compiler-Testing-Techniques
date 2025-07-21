'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
_input_tensor = torch.randint(0, 180, (3, 3))
print('Input: ', _input_tensor)
_output_tensor = torch.Tensor.deg2rad(_input_tensor)
print('Output: ', _output_tensor)