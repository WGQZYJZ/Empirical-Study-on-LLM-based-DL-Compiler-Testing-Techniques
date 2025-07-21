'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.equal\ntorch.equal(input, other)\n'
import torch
input1 = torch.rand(3, 5)
input2 = torch.rand(3, 5)
result = torch.equal(input1, input2)
print(result)