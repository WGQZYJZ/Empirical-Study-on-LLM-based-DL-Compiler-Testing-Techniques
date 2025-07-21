'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.vstack\ntorch.vstack(tensors, *, out=None)\n'
import torch
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)
tensor3 = torch.randn(2, 3)
result = torch.vstack([tensor1, tensor2, tensor3])
print(result)