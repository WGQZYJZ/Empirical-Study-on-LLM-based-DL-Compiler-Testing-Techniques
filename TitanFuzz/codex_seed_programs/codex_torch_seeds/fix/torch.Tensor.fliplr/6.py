'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fliplr\ntorch.Tensor.fliplr(_input_tensor)\n'
import torch
input_data = torch.arange(20).view(4, 5)
print(input_data)
print(input_data.fliplr(input_data))