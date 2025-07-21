'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.polygamma\ntorch.special.polygamma(n, input, *, out=None)\n'
import torch
input_data = torch.rand(10)
polygamma_1 = torch.special.polygamma(1, input_data)
polygamma_2 = torch.special.polygamma(2, input_data)
print('polygamma_1 is: ', polygamma_1)
print('polygamma_2 is: ', polygamma_2)