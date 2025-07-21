"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.fork_rng\ntorch.random.fork_rng(devices=None, enabled=True, _caller='fork_rng', _devices_kw='devices')\n"
import torch
input = torch.rand(10, 2)
torch.random.fork_rng(devices=[0, 1])
input2 = torch.rand(10, 2)
torch.random.fork_rng(devices=None)
input3 = torch.rand(10, 2)
print('input1: ', input)
print('input2: ', input2)
print('input3: ', input3)