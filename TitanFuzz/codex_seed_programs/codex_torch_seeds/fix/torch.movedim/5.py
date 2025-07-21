'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.movedim\ntorch.movedim(input, source, destination)\n'
import torch
input_data = torch.randn(2, 3, 4)
print(input_data)
output = torch.movedim(input_data, 0, 1)
print(output)