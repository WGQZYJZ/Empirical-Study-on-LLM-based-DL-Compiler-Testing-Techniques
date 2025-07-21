'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Sampler\ntorch.utils.data.Sampler(data_source)\n'
import torch
import torch.utils.data
import torch
x = torch.randn(10, 3)
y = torch.randint(0, 2, (10,))
torch.utils.data.Sampler(data_source=None)