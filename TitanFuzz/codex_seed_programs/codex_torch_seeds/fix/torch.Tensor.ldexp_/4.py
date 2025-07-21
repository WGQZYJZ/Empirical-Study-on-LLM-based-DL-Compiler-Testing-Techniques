'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ldexp_\ntorch.Tensor.ldexp_(_input_tensor, other)\n'
import torch
import numpy as np
tensor = torch.randn(1, 3, 5)
tensor = tensor.ldexp_(1)
print(tensor)