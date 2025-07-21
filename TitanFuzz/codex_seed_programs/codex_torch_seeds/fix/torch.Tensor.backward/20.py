'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
input_tensor = torch.randn(3, 3, requires_grad=True)
input_tensor.backward(torch.ones(3, 3))
print(input_tensor.grad)