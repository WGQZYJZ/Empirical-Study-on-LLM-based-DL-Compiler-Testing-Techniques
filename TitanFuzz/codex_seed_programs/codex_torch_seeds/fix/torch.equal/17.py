'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
tensor_a = torch.randn(3, 3)
tensor_b = torch.randn(3, 3)
result = torch.equal(tensor_a, tensor_b)
print(result)