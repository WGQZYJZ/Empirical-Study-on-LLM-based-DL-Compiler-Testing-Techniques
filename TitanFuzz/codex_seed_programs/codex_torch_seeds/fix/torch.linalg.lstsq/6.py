'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.lstsq\ntorch.linalg.lstsq(A, B, rcond=None, *, driver=None)\n'
import torch
features = torch.randn((1, 3))
labels = torch.randn((1, 1))
weights = torch.linalg.lstsq(features, labels)
print(weights)