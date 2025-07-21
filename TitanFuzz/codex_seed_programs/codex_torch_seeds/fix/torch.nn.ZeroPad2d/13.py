'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
input = torch.tensor([[[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]]], dtype=torch.float32)
padding = (2, 2, 2, 2)
zero_pad = torch.nn.ZeroPad2d(padding)
output = zero_pad(input)
print('Input: ', input)
print('Output: ', output)