'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.storage\ntorch.Tensor.storage(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(2, 3, 4)
print('Input tensor: ', _input_tensor)
torch.Tensor.storage(_input_tensor)