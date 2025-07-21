'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.logit\ntorch.Tensor.logit(_input_tensor)\n'
import torch
import numpy as np
import torch
input_tensor = torch.rand(2, 3, 4, 5)
print('input_tensor:', input_tensor)
logit_tensor = torch.Tensor.logit(input_tensor)
print('logit_tensor:', logit_tensor)