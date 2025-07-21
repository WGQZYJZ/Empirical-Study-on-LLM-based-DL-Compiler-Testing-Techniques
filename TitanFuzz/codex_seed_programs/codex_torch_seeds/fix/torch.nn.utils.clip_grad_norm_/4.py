'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.clip_grad_norm_\ntorch.nn.utils.clip_grad_norm_(parameters, max_norm, norm_type=2.0, error_if_nonfinite=False)\n'
import torch
input_data = torch.randn(10, 10)
torch.nn.utils.clip_grad_norm_(input_data, max_norm=1.0, norm_type=2.0, error_if_nonfinite=True)