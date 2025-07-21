'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.nextafter_\ntorch.Tensor.nextafter_(_input_tensor, other)\n'
import torch
_input_tensor = torch.rand(4, 4)
other = torch.rand(4, 4)
_out_tensor = torch.Tensor.nextafter_(_input_tensor, other)
print(_out_tensor)