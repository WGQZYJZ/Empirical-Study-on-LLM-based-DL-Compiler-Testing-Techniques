'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_rng_state\ntorch.set_rng_state(new_state)\n'
import torch
x = torch.randn(1, requires_grad=True)
y = torch.randn(1, requires_grad=True)
torch.set_rng_state(torch.get_rng_state())
z = (x + y)
z.backward()
print(x.grad, y.grad)