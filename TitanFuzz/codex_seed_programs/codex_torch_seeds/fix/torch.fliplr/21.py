'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fliplr\ntorch.fliplr(input)\n'
import torch
data = torch.arange(1, 9).view(2, 2, 2)
print('Input data:')
print(data)
result = torch.fliplr(data)
print('Output of torch.fliplr:')
print(result)