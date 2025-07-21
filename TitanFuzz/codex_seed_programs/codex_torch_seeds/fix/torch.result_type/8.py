'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.result_type\ntorch.result_type(tensor1, tensor2)\n'
import torch
a = torch.randn(3, 4)
b = torch.randn(4, 5)
print(torch.result_type(a, b))