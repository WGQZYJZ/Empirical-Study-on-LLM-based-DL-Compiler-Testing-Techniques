'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_warn_always\ntorch.set_warn_always(b)\n'
import torch
x = torch.tensor([1, 2, 3])
y = torch.tensor([4, 5, 6])
torch.set_warn_always(True)
z = (x + y)
print(z)
torch.set_warn_always(False)
z = (x + y)
print(z)