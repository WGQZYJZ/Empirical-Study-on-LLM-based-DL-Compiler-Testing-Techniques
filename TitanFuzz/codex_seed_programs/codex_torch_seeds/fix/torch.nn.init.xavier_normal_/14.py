'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
tensor = torch.rand(2, 2)
print('\nTensor: ', tensor)
torch.nn.init.xavier_normal_(tensor, gain=1.0)
print('\nTensor after Xavier Normal: ', tensor)