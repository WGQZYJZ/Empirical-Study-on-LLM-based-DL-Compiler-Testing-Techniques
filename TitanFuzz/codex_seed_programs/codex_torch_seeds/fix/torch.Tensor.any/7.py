'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.any\ntorch.Tensor.any(_input_tensor, dim=None, keepdim=False)\n'
import torch
import torch
_input_tensor = torch.randint(0, 2, (3, 4, 5), dtype=torch.float)
_output_tensor = torch.Tensor.any(_input_tensor, dim=None, keepdim=False)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)