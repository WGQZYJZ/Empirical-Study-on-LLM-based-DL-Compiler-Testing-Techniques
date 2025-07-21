'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
tensor_a = torch.randn(1, 3)
tensor_b = torch.randn(3, 1)
tensor_c = torch.broadcast_tensors(tensor_a, tensor_b)
print(tensor_c)