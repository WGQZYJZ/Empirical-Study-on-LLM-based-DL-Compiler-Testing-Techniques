"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.fork_rng\ntorch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')\n"
import torch
input_data = torch.randn(3, 3)
print('input_data:', input_data)
torch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')