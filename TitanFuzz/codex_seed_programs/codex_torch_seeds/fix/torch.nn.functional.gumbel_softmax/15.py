'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
import torch.nn.functional as F
import torch
input_data = torch.randn(3, 5)
output = F.gumbel_softmax(input_data)
print(output)