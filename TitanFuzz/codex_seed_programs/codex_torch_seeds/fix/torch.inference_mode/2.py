'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inference_mode\ntorch.inference_mode(mode=True)\n'
import torch
x = torch.randn(1, 1, 224, 224)
print(x.shape)
torch.inference_mode(mode=True)
print(x.shape)