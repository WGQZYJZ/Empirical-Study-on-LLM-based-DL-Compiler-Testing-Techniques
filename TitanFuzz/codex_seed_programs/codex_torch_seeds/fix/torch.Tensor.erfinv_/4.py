'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfinv_\ntorch.Tensor.erfinv_(_input_tensor)\n'
import torch
import numpy as np
input_tensor = torch.tensor(np.random.rand(10, 10))
torch.Tensor.erfinv_(input_tensor)