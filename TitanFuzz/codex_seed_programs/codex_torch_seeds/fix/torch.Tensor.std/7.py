'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.std\ntorch.Tensor.std(_input_tensor, dim, unbiased=True, keepdim=False)\n'
import torch
_input_tensor = torch.randn(3, 4)
print('_input_tensor: ', _input_tensor)
_output_tensor = torch.Tensor.std(_input_tensor, dim=0)
print('_output_tensor: ', _output_tensor)