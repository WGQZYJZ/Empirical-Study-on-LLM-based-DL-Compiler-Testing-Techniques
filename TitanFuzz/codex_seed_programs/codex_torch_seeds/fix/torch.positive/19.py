'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
x = torch.randn(3, requires_grad=True)
print(x)
y = torch.positive(x)
print(y)
y.backward(torch.tensor([1.0, 1.0, 1.0]))
print(x.grad)