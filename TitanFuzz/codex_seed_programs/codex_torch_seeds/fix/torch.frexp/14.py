'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.frexp\ntorch.frexp(input, *, out=None)\n'
import torch
data = torch.rand(4, 4)
print('The input data is:\n{}'.format(data))
data_frexp = torch.frexp(data)
print('The output of torch.frexp is:\n{}'.format(data_frexp))