'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multiply_\ntorch.Tensor.multiply_(_input_tensor, value)\n'
import torch
input_tensor = torch.randn(2, 3)
torch.Tensor.multiply_(input_tensor, 2)
print(input_tensor)
'\nTask 4: Call the API torch.Tensor.div_\ntorch.Tensor.div_(_input_tensor, value)\n'
torch.Tensor.div_(input_tensor, 2)
print(input_tensor)
'\nTask 5: Call the API torch.Tensor.zero_\ntorch.Tensor.zero_(_input_tensor)\n'
torch.Tensor.zero_(input_tensor)
print(input_tensor)
'\nTask 6: Call the API torch.Tensor.fill_\ntorch.Tensor.fill_(_input_tensor, value)\n'
torch.Tensor.fill_(input_tensor, 2)
print(input_tensor)