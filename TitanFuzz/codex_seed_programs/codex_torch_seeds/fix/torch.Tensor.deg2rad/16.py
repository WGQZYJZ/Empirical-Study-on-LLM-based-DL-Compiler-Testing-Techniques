'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.deg2rad\ntorch.Tensor.deg2rad(_input_tensor)\n'
import torch
_input_tensor = torch.tensor([180.0, (- 90.0), 360.0, (- 45.0)])
_output_tensor = torch.Tensor.deg2rad(_input_tensor)
print('The input tensor is:', _input_tensor)
print('The output tensor is:', _output_tensor)