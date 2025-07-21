'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
x = torch.tensor([(- 1), 0, 1], dtype=torch.float)
softplus = torch.nn.Softplus(beta=1, threshold=20)
y = softplus(x)
print('Input: {}'.format(x))
print('Output: {}'.format(y))