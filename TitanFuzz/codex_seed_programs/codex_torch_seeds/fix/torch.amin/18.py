'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amin\ntorch.amin(input, dim, keepdim=False, *, out=None)\n'
import torch
input = torch.randn(3, 4)
print('Input data: \n{}'.format(input))
print('Dim=0: \n{}'.format(torch.amin(input, dim=0)))
print('Dim=1: \n{}'.format(torch.amin(input, dim=1)))
print('Dim=0, keepdim=True: \n{}'.format(torch.amin(input, dim=0, keepdim=True)))
print('Dim=1, keepdim=True: \n{}'.format(torch.amin(input, dim=1, keepdim=True)))
print('Dim=(0, 1): \n{}'.format(torch.amin(input, dim=(0, 1))))