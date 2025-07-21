'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)\n'
import torch
import torch.nn.utils as utils
input_data = torch.randn(10, 5)
utils.clip_grad_norm_(input_data, max_norm=0.5)