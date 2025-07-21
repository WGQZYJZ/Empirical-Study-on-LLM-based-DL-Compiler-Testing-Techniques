'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([30.0, 60.0, 90.0, 120.0, 150.0, 180.0, 210.0, 240.0, 270.0, 300.0, 330.0])
print('Input Tensor : {}'.format(_input_tensor))
_output_tensor = torch.Tensor.deg2rad(_input_tensor)
print('Output Tensor : {}'.format(_output_tensor))