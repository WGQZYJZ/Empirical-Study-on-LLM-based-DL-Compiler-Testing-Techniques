'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inference_mode\ntorch.inference_mode(mode=True)\n'
import torch
input_data = torch.rand(1, 3, 224, 224)
torch.inference_mode(mode=True)