'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.local_response_norm\ntorch.nn.functional.local_response_norm(input, size, alpha=0.0001, beta=0.75, k=1.0)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 3, 5, 5)
print(F.local_response_norm(input, size=2, alpha=0.0001, beta=0.75, k=1.0))