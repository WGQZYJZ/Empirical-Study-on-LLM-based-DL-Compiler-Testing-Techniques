'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
tensors = []
for i in range(4):
    tensors.append(torch.rand(3, 4))
result = torch.broadcast_tensors(*tensors)
print(result)