'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'
import torch
import numpy as np
import torch
_input_tensor = torch.randn(2, 3, 224, 224)
torch.Tensor.to_mkldnn(_input_tensor)
'\n# Task 1: import PyTorch\nimport torch\n# Task 2: Generate input data\n_input_tensor = torch.randn(2, 3, 224, 224)\n# Task 3: Call the API torch.Tensor.to_mkldnn\ntorch.Tensor.to_mkldnn(_input_tensor)\n'