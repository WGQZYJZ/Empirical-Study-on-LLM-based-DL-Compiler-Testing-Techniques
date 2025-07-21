'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.angle\ntorch.Tensor.angle(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 4)
print(input_tensor)
angle_tensor = torch.Tensor.angle(input_tensor)
print(angle_tensor)
'\nTask 4: Call the API torch.Tensor.diag\ntorch.Tensor.diag(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
diag_tensor = torch.Tensor.diag(input_tensor)
print(diag_tensor)
'\nTask 5: Call the API torch.Tensor.trace\ntorch.Tensor.trace(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 4)
print(input_tensor)
trace_tensor = torch.Tensor.trace(input_tensor)
print(trace_tensor)