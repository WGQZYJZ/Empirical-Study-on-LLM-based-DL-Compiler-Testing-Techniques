'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tensor_split\ntorch.tensor_split(input, indices_or_sections, dim=0)\n'
import torch
input_data = torch.randn(10)
print(input_data)
print(input_data.shape)
tensor_split = torch.tensor_split(input_data, 5, dim=0)
print(tensor_split)
for i in range(len(tensor_split)):
    print(tensor_split[i])