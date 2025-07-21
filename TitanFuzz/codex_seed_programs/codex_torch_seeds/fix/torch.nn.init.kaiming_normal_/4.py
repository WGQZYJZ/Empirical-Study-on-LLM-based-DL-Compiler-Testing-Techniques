"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_normal_\ntorch.nn.init.kaiming_normal_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
input_data = torch.randn(1, 3, 32, 32)
print(input_data.shape)
output_data = torch.nn.init.kaiming_normal_(input_data)
print(output_data.shape)
input_data = torch.randn(1, 3, 32, 32)
print(input_data.shape)
output_data = torch.nn.init.kaiming_normal_(input_data, nonlinearity='relu')
print(output_data.shape)