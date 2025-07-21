'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcdiv\ntorch.addcdiv(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
input = torch.randn(3, 3, requires_grad=True)
tensor1 = torch.ones(3, 3, dtype=torch.float32)
tensor2 = torch.ones(3, 3, dtype=torch.float32)
output = torch.addcdiv(input, tensor1, tensor2)
print(output)