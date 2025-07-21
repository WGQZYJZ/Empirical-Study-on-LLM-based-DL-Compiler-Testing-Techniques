'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.square\ntorch.square(input, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=torch.float32)
output_data = torch.square(input_data)
print(output_data)
mean_output = torch.mean(output_data)
print(mean_output)
sum_output = torch.sum(output_data)
print(sum_output)