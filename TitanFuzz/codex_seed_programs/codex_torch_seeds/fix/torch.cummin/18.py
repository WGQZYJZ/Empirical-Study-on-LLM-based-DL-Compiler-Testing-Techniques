'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummin\ntorch.cummin(input, dim, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print(input)
cummin = torch.cummin(input, dim=1)
print(cummin)
'\nOutput:\ntensor([[ 0.7105,  0.7599, -0.8016, -0.0659],\n        [ 0.1857, -0.0706, -0.9079,  0.7472],\n        [-0.7207,  0.0134, -0.3340,  0.6368]])\ntensor([[ 0.7105,  0.7599, -0.8016, -0.8016],\n        [ 0.1857,  0.1857, -0.9079, -0.9079],\n        [-0.7207, -0.7207, -0.7207, -0.7207]])\n'