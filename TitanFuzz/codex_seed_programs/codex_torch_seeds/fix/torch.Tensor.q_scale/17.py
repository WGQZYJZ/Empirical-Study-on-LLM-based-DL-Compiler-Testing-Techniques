'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.q_scale\ntorch.Tensor.q_scale(_input_tensor)\n'
import torch
import numpy as np
_input_tensor = torch.randn(1, 3, 224, 224)
torch.Tensor.q_scale(_input_tensor)