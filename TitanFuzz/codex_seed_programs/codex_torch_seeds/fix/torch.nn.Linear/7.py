'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
x = torch.randn(1, 3)
print('x: ', x)
linear_model = torch.nn.Linear(3, 1)
print('linear_model: ', linear_model)
print('linear_model.weight: ', linear_model.weight)
print('linear_model.bias: ', linear_model.bias)
y = linear_model(x)
print('y: ', y)
y.backward()
print('linear_model.weight.grad: ', linear_model.weight.grad)
print('linear_model.bias.grad: ', linear_model.bias.grad)