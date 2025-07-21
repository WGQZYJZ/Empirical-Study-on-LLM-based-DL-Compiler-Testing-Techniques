'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
_input_tensor = torch.randn(3, 5, requires_grad=True)
_input_tensor = _input_tensor.to_mkldnn()
_output_tensor = torch.randn(3, 5, requires_grad=True)
_output_tensor = _output_tensor.to_mkldnn()