'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch._assert\ntorch._assert(condition, message)\n'
import torch
x = torch.randn((1, 2, 3, 4))
torch._assert((x.shape == (1, 2, 3, 4)), 'x.shape is not (1, 2, 3, 4)')