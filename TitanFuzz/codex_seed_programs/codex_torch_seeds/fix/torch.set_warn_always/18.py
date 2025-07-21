'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
x = torch.tensor([[1, 2], [3, 4]])
y = torch.tensor([[5, 6], [7, 8]])
torch.set_warn_always(True)
print('x + y = ', (x + y))
torch.set_warn_always(False)
print('x + y = ', (x + y))
torch.set_warn_always(True)
print('x + y = ', (x + y))
torch.set_warn_always(False)
print('x + y = ', (x + y))