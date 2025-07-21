'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5, dtype=torch.float32, requires_grad=True)
torch.Tensor.qscheme(input_tensor)