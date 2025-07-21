'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_inference_mode_enabled\ntorch.is_inference_mode_enabled()\n'
import torch
x = torch.rand(10)
print('Input data: ', x)
print('\nInference mode: ', torch.is_inference_mode_enabled())