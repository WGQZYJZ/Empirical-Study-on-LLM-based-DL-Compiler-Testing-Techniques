'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.erfinv\ntorch.Tensor.erfinv(_input_tensor)\n'
import torch
import numpy as np
input_data = np.random.randn(4, 4)
input_data = torch.Tensor(input_data)
torch.Tensor.erfinv(input_data)