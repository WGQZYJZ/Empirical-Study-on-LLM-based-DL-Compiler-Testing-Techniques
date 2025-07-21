"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.fork_rng\ntorch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')\n"
import torch
print(torch.__version__)
a = torch.rand(2, 3)
print(a)
torch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')
print(torch.rand(2, 3))