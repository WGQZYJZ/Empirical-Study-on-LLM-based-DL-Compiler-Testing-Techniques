'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.addcmul\ntorch.addcmul(input, tensor1, tensor2, *, value=1, out=None)\n'
import torch
import numpy as np
input = torch.randn(2, 3)
tensor1 = torch.randn(2, 3)
tensor2 = torch.randn(2, 3)
print('Input: ', input)
print('tensor1: ', tensor1)
print('tensor2: ', tensor2)
output = torch.addcmul(input, tensor1, tensor2)
print('Output: ', output)