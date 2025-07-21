'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
import torch.nn.functional as F
logits = torch.randn(2, 3)
gumbel_softmax_output = F.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=(- 1))
print(gumbel_softmax_output)
gumbel_softmax_output = F.gumbel_softmax(logits, tau=1, hard=True, eps=1e-10, dim=(- 1))
print(gumbel_softmax_output)