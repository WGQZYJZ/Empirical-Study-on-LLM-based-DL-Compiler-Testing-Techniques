'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fix_\ntorch.Tensor.fix_(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(4, 4, dtype=torch.float32)
_input_tensor = _input_tensor.cuda()
torch.Tensor.fix_(_input_tensor)