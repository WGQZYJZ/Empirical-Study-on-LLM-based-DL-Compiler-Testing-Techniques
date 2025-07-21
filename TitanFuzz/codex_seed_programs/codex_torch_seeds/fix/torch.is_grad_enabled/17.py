'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.is_grad_enabled\ntorch.is_grad_enabled()\n'
import torch
data = torch.rand(3, 4)
torch.is_grad_enabled()
torch.set_grad_enabled(False)
torch.is_grad_enabled()
torch.set_grad_enabled(True)
torch.is_grad_enabled()