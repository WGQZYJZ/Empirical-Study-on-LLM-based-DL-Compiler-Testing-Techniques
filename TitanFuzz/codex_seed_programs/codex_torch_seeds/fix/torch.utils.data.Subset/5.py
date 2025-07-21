'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
input_data = torch.arange(0, 10)
print(input_data)
indices = [3, 4, 5]
output_data = torch.utils.data.Subset(input_data, indices)
print(output_data)