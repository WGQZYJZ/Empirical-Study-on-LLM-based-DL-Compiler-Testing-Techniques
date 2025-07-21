'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
x = torch.randn(1, 1)
x = x.cuda()
y = torch.nn.functional.softplus(x)
print(y)