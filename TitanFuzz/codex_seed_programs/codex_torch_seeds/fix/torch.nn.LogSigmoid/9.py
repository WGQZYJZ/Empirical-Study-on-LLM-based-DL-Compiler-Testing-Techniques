'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LogSigmoid\ntorch.nn.LogSigmoid()\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.nn.LogSigmoid()(x)
print(y)
y.backward(torch.tensor([1, 0.1, 0.01]))
print(x.grad)