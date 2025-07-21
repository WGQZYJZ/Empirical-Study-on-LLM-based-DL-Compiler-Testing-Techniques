'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
import torch.nn.functional as F
logits = torch.randn(2, 3)
print(logits)
print(F.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1)))
input_data = torch.randn(4, 2, 3)
print(input_data)
print(F.gumbel_softmax(input_data, tau=1, hard=False, eps=1e-10, dim=(- 1)))