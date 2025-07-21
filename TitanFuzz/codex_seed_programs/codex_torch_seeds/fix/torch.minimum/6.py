'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.minimum\ntorch.minimum(input, other, *, out=None)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
other_tensor = torch.randn(2, 3)
torch.minimum(input_tensor, other_tensor)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.min\ntorch.min(input)\ntorch.min(input, dim, keepdim=False, *, out=None) -> (Tensor, LongTensor)\n'
import torch
import torch
input_tensor = torch.randn(2, 3)
torch.min(input_tensor)
torch.min(input_tensor, dim=0, keepdim=False)