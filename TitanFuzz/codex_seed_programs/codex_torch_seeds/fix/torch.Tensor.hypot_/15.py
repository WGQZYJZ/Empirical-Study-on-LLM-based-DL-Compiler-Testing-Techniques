'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot_\ntorch.Tensor.hypot_(_input_tensor, other)\n'
import torch
data_tensor = torch.rand(2, 3)
other_tensor = torch.rand(2, 3)
torch.Tensor.hypot_(data_tensor, other_tensor)