'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
import torch.nn.functional as F
'\nTask 1: import PyTorch\n'
'\nTask 2: Generate input data\n'
input_data = torch.randn(3, 5)
'\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
output = F.gumbel_softmax(input_data, hard=True)
print(output)