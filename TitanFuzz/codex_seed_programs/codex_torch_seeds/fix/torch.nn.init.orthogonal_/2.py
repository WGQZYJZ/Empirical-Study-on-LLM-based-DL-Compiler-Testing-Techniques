'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
tensor = torch.Tensor(3, 3)
tensor.fill_(0)
print('Input data:')
print(tensor)
torch.nn.init.orthogonal_(tensor, gain=1)
print('Output data:')
print(tensor)