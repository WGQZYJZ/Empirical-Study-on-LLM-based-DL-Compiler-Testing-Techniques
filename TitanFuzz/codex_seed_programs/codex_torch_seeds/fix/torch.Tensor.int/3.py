'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.int\ntorch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(2, 3, 4)
torch.Tensor.int(_input_tensor, memory_format=torch.preserve_format)