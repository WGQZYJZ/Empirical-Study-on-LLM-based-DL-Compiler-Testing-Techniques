'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
_input_tensor = torch.randint(low=1, high=5, size=(3, 2, 4))
print('Input tensor: ', _input_tensor)
_output_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)
print('Output tensor: ', _output_tensor)
_output_tensor = torch.Tensor.any(_input_tensor, dim=1, keepdim=False)
print('Output tensor: ', _output_tensor)
_output_tensor = torch.Tensor.any(_input_tensor, dim=1, keepdim=True)
print('Output tensor: ', _output_tensor)