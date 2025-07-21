'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)\n'
import torch
import numpy as np
parameters = [(torch.ones(10, 10) * 0.1), (torch.ones(10, 10) * 0.1)]
max_norm = 1.0
norm_type = 2.0
error_if_nonfinite = False
torch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type, error_if_nonfinite)