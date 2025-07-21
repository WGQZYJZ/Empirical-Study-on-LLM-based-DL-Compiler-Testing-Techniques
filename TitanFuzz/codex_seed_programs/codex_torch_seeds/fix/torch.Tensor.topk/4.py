'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.topk\ntorch.Tensor.topk(_input_tensor, k, dim=None, largest=True, sorted=True)\n'
import torch
input_tensor = torch.randn(3, 5)
print('input_tensor =', input_tensor)
k = 2
dim = 1
largest = True
sorted = True
topk_tensor = input_tensor.topk(k, dim, largest, sorted)
print('topk_tensor =', topk_tensor)