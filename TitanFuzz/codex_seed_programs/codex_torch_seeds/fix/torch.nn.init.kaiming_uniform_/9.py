"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.kaiming_uniform_\ntorch.nn.init.kaiming_uniform_(tensor, a=0, mode='fan_in', nonlinearity='leaky_relu')\n"
import torch
input_size = 10
output_size = 5
input_data = torch.randn(input_size, output_size)
torch.nn.init.kaiming_uniform_(input_data)
print(input_data)