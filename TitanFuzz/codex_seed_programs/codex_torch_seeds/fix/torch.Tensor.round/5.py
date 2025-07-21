'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.round\ntorch.Tensor.round(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
torch.Tensor.round(_input_tensor)
torch.round(_input_tensor)
torch.round(_input_tensor, out=None)