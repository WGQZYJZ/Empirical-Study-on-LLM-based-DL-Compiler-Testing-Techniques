'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapdims\ntorch.swapdims(input, dim0, dim1)\n'
import torch
input_data = torch.randn(3, 4, 5)
output_data = torch.swapdims(input_data, 0, 2)
print(output_data.size())