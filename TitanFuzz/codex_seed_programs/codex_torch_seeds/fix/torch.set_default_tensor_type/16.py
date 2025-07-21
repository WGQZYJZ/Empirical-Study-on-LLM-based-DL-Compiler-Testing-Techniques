'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_default_tensor_type\ntorch.set_default_tensor_type(t)\n'
import torch
input_data = torch.randn(2, 3, 5)
print(input_data)
torch.set_default_tensor_type(torch.FloatTensor)
print(input_data)