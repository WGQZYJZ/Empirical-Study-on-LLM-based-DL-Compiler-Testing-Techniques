'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
sign_data = torch.sign(input_data)
print(sign_data)