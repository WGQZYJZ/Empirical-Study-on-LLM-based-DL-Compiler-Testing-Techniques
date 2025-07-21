'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sigmoid_\ntorch.Tensor.sigmoid_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
output_tensor = torch.Tensor.sigmoid_(input_tensor)
print(output_tensor)
print(torch.sigmoid(input_tensor))
'\nTask 4: Call the API torch.Tensor.tanh_\ntorch.Tensor.tanh_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)
output_tensor = torch.Tensor.tanh_(input_tensor)
print(output_tensor)
print(torch.tanh(input_tensor))
'\nTask 5: Call the API torch.Tensor.relu_\ntorch.Tensor.relu_(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 3)
print(input_tensor)