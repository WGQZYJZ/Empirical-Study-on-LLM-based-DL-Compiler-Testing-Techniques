"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.fork_rng\ntorch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')\n"
import torch
x = torch.randn(1)
torch.random.fork_rng(devices=[0, 1])