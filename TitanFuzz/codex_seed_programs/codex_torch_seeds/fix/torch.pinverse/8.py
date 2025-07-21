'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
input_data = torch.randn(2, 3)
print('Input Data: ', input_data)
pinverse_data = torch.pinverse(input_data)
print('Pinverse Data: ', pinverse_data)