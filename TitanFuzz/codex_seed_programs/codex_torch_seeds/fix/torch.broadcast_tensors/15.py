'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
t1 = torch.tensor([[1, 2], [3, 4]])
t2 = torch.tensor([[9], [10]])
print(t1)
print(t2)
t3 = torch.broadcast_tensors(t1, t2)
print(t3)
print(t3[0])
print(t3[1])