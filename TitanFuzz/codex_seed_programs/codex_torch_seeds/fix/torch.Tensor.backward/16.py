'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
a = torch.tensor(2, dtype=torch.float32, requires_grad=True)
b = torch.tensor(3, dtype=torch.float32, requires_grad=True)
c = torch.tensor(4, dtype=torch.float32, requires_grad=True)
d = ((a * b) + c)
d.backward()
print(a.grad)
print(b.grad)
print(c.grad)