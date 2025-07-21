'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.broadcast_tensors\ntorch.broadcast_tensors(*tensors)\n'
import torch
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 1)
tensor_list = torch.broadcast_tensors(tensor1, tensor2)
print(tensor_list)