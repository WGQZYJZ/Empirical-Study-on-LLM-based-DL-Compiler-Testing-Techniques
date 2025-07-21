'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
input_data = torch.arange(1, 17).view(4, 4)
print(input_data)
output_data = torch.fliplr(input_data)
print(output_data)