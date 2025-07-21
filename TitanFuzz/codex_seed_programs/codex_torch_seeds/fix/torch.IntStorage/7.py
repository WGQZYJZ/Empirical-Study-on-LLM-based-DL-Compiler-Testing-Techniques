'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.IntStorage\ntorch.IntStorage(*args, **kwargs)\n'
import torch
a = torch.IntTensor([1, 2, 3, 4, 5])
b = torch.IntTensor([6, 7, 8, 9, 10])
c = torch.IntStorage(a.size()[0])
for i in range(a.size()[0]):
    c[i] = (a[i] + b[i])
print(c)