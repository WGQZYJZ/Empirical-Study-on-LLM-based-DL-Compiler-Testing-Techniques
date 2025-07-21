'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.is_pinned\ntorch.Tensor.is_pinned(_input_tensor, )\n'
import torch
import numpy as np
_input_tensor = torch.rand(10, 10)
_result = torch.Tensor.is_pinned(_input_tensor)
print('result: ', _result)