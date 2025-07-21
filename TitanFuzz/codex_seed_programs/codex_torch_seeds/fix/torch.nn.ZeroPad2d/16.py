'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]], dtype=torch.float32)
padding = (1, 1, 2, 2)
zero_pad = torch.nn.ZeroPad2d(padding)
result = zero_pad(data)
print('result:', result)