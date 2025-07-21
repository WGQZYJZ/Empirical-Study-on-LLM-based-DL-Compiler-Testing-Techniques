'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
print(x)
y = (x + 2)
print(y)
y.backward()
print(x.grad)