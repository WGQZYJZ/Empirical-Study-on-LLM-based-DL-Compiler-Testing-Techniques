'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
x = torch.ones(2, 2, requires_grad=True)
print(x)
y = (x + 2)
print(y)
z = ((y * y) * 3)
out = z.mean()
print(z, out)
out.backward()
print(x.grad)