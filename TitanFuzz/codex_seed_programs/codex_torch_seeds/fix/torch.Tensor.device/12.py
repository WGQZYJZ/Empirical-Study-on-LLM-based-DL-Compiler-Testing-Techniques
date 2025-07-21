'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.device\ntorch.Tensor.device(_input_tensor, )\n'
import torch
_input_tensor = torch.rand((10,))
_device = torch.Tensor.device(_input_tensor)
print(_device)