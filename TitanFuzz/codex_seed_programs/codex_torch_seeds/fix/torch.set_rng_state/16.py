'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
import torch
x = torch.randn(3, 3)
y = torch.randn(3, 3)
new_state = torch.get_rng_state()
torch.set_rng_state(new_state)
print(torch.randn(3, 3))
print(torch.randn(3, 3))
print(torch.randn(3, 3))
print('x is equal to y: {}'.format(torch.all(torch.eq(x, y))))