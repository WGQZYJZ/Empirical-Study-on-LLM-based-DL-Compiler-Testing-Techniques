'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_num_interop_threads\ntorch.set_num_interop_threads(int)\n'
import torch
input_data = torch.randn(1, 1, 28, 28)
torch.set_num_interop_threads(1)
conv = torch.nn.Conv2d(1, 1, 3)
output = conv(input_data)
print(output)