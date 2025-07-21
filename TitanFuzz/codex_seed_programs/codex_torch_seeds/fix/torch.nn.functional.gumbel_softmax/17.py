'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
import torch
input_data = torch.randn(4, 4)
input_data.requires_grad = True
output = torch.nn.functional.gumbel_softmax(input_data, tau=1, hard=False, eps=1e-10, dim=(- 1))
print(output)
output.backward(torch.ones(output.size()))
print(input_data.grad)