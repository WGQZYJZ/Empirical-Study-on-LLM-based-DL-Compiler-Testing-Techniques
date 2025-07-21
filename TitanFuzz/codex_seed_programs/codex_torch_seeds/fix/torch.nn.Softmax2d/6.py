'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d()\n'
import torch
(batch_size, in_channel, height, width) = (2, 3, 4, 5)
input = torch.randn(batch_size, in_channel, height, width)
output = torch.nn.Softmax2d()(input)
print(output)