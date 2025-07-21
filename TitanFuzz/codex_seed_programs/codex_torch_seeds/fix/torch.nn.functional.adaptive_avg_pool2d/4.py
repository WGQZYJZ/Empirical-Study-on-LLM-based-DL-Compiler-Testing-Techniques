'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool2d\ntorch.nn.functional.adaptive_avg_pool2d(input, output_size)\n'
import torch
input_data = torch.arange(1, 17, dtype=torch.float32).view(1, 1, 4, 4)
output_size = (3, 3)
output = torch.nn.functional.adaptive_avg_pool2d(input_data, output_size)
print(output)