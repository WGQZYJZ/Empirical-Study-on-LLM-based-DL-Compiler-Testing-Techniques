'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 3, dtype=torch.float16)
print(torch.Tensor.qscheme(_input_tensor))