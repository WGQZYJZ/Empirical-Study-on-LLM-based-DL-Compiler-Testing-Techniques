'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.get_num_threads\ntorch.get_num_threads()\n'
import torch
input_data = torch.randn(1, 1, 28, 28)
print('Number of threads before:', torch.get_num_threads())
torch.set_num_threads(4)
print('Number of threads after:', torch.get_num_threads())
conv1 = torch.nn.Conv2d(in_channels=1, out_channels=6, kernel_size=3, stride=1)
conv2 = torch.nn.Conv2d(in_channels=6, out_channels=16, kernel_size=3, stride=1)
output = conv1(input_data)
output = conv2(output)
print('Output shape:', output.shape)