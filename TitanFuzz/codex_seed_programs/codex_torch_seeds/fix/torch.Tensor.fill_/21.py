'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
import torch
_input_tensor = torch.Tensor(2, 3)
_input_tensor.fill_(10)
print(_input_tensor)