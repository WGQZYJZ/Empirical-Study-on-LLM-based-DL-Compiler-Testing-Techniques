'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_inference_mode_enabled\ntorch.is_inference_mode_enabled()\n'
import torch
x = torch.randn(1, 1, 1, 1)
print(torch.is_inference_mode_enabled())