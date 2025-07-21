'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.jit.wait\ntorch.jit.wait(future)\n'
import torch
import time
input = torch.randn(1, 1, 32, 32)
future = torch.jit._fork(torch.sum, input)
torch.jit.wait(future)
print('The result of torch.sum(input) is: ', future.value())