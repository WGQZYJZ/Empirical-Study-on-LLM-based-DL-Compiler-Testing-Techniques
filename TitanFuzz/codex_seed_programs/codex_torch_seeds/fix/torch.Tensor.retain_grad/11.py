'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.tensor(np.random.randn(4, 4), requires_grad=True)
_input_tensor.retain_grad()