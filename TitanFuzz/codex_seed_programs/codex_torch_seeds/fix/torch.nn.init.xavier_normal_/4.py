'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
xavier_normal_tensor = torch.randn(2, 3)
print(xavier_normal_tensor)
torch.nn.init.xavier_normal_(xavier_normal_tensor)
print(xavier_normal_tensor)