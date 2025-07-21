'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LeakyReLU\ntorch.nn.LeakyReLU(negative_slope=0.01, inplace=False)\n'
import torch
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
leaky_relu = torch.nn.LeakyReLU(negative_slope=0.01, inplace=False)
output_data = leaky_relu(input_data)
print('input_data:', input_data)
print('output_data:', output_data)