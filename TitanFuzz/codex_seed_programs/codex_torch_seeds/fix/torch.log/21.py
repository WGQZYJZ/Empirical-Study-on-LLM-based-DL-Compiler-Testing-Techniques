'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log\ntorch.log(input, *, out=None)\n'
import torch
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.log(x)
print('The result of torch.log(x) is: ', y)