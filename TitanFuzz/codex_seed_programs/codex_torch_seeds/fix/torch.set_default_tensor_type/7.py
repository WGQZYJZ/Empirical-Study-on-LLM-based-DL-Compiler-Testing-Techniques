'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(torch.get_default_dtype())
torch.set_default_tensor_type(torch.DoubleTensor)
print(torch.get_default_dtype())
input_data = torch.randn(2, 3)
print(input_data)
'\nTask 4: Call the API torch.set_default_dtype\ntorch.set_default_dtype(d)\n'
print(torch.get_default_dtype())
torch.set_default_dtype(torch.float32)
print(torch.get_default_dtype())
input_data = torch.randn(2, 3)
print(input_data)
'\nTask 5: Call the API torch.get_default_dtype\ntorch.get_default_dtype()\n'
print(torch.get_default_dtype())