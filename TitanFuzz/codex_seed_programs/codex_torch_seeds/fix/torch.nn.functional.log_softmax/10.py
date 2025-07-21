'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.log_softmax\ntorch.nn.functional.log_softmax(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
import torch
input = torch.randn(2, 3, requires_grad=True)
output = torch.nn.functional.log_softmax(input, dim=1)
print(output)