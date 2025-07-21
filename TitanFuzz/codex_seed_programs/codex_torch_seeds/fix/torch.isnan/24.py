'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isnan\ntorch.isnan(input)\n'
import torch
input_data = torch.randn(2, 3, 4)
input_data[0][0][0] = float('nan')
input_data[0][1][1] = float('nan')
input_data[1][2][2] = float('nan')
output = torch.isnan(input_data)
print(output)