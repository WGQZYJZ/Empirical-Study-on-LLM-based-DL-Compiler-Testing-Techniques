'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
tensor1 = torch.rand(3, 3)
tensor2 = torch.rand(3, 3)
tensor3 = torch.rand(3, 3)
torch.addcdiv(tensor1, tensor2, tensor3, value=1)
torch.addcdiv(tensor1, tensor2, tensor3, value=1, out=tensor1)