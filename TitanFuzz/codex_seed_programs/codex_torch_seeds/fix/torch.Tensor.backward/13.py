'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.backward\ntorch.Tensor.backward(_input_tensor, gradient=None, retain_graph=None, create_graph=False, inputs=None)\n'
import torch
import torch.nn as nn
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
y = (x * 2)
y.backward(torch.tensor([1.0, 1.0, 1.0]))
print(x.grad)