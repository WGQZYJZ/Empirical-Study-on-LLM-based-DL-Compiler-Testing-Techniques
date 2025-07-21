'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.multi_dot\ntorch.linalg.multi_dot(tensors, *, out=None)\n'
import torch
tensors = []
for i in range(5):
    tensors.append(torch.randn(10, 10))
result = torch.linalg.multi_dot(tensors)
print(result)