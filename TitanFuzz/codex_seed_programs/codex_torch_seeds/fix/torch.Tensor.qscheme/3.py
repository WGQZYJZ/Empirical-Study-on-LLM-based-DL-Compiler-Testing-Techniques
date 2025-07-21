'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.qscheme\ntorch.Tensor.qscheme(_input_tensor)\n'
import torch
_input_tensor = torch.rand(4, 4)
_input_tensor.qscheme()
_input_tensor.qscheme(torch.per_tensor_symmetric)