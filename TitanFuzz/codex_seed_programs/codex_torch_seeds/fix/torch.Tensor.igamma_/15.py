'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.igamma_\ntorch.Tensor.igamma_(_input_tensor, other)\n'
import torch
_input_tensor = torch.randint(1, 10, (3, 3), dtype=torch.float32)
other = torch.randint(1, 10, (3, 3), dtype=torch.float32)
torch.Tensor.igamma_(_input_tensor, other)
print(_input_tensor)