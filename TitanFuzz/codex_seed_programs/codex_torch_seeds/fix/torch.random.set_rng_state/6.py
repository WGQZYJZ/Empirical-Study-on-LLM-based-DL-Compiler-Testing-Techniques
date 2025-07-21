'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.set_rng_state\ntorch.random.set_rng_state(new_state)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
data = torch.rand(2, 3)
print('data: ', data)
print('Task 3: Call the API torch.random.set_rng_state')
rng_state = torch.get_rng_state()
print('rng_state: ', rng_state)
torch.random.set_rng_state(rng_state)
data = torch.rand(2, 3)
print('data: ', data)