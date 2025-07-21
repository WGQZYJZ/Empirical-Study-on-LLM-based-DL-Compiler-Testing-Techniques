'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.pin_memory\ntorch.Tensor.pin_memory(_input_tensor)\n'
import torch
input_tensor = torch.randn(3, 2, requires_grad=True)
pin_tensor = input_tensor.pin_memory()
print(input_tensor)
print(pin_tensor)