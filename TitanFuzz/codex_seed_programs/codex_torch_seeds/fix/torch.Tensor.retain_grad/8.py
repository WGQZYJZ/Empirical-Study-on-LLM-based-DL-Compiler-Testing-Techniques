'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.retain_grad\ntorch.Tensor.retain_grad(_input_tensor)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = (x * 2)
while (y.data.norm() < 1000):
    y = (y * 2)
print(y)
y.retain_grad()
v = torch.tensor([0.1, 1.0, 0.0001], dtype=torch.float)
y.backward(v)
print(x.grad)