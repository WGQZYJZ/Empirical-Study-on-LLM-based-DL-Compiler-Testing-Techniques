'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
pinv_data = torch.pinverse(input_data)
print(pinv_data)
print(torch.mm(input_data, pinv_data))
print(torch.mm(pinv_data, input_data))