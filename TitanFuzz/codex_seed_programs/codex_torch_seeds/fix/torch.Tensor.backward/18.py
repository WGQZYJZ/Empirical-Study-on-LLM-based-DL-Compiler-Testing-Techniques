'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
x = torch.tensor([1.0, 2.0, 3.0, 4.0], requires_grad=True)
y = (2 * x)
z = y.view(2, 2)
print(z)
v = torch.tensor([[1.0, 0.1], [0.01, 0.001]], dtype=torch.float)
z.backward(v)
print(x.grad)