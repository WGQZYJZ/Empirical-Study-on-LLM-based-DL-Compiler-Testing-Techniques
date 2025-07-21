'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
input_data = torch.rand(1, 1, 3, 3)
print(input_data)
with torch.no_grad():
    output_data = torch.relu(input_data)
    print(output_data)