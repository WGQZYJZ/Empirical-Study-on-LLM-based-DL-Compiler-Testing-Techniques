'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
input_data = torch.randn(1, 5, requires_grad=True)
print(input_data)
linear_model = torch.nn.Linear(5, 1)
print(linear_model)
output_data = linear_model(input_data)
print(output_data)
print(linear_model.weight)
print(linear_model.bias)
print(linear_model.weight.grad)
print(linear_model.bias.grad)
loss_function = torch.nn.MSELoss()
loss = loss_function(output_data, torch.randn(1, 1))
print(loss)
loss.backward()
print(linear_model.weight.grad)
print(linear_model.bias.grad)