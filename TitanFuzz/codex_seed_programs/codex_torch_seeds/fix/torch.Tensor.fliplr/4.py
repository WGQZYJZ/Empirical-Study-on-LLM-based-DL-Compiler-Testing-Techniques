'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.fliplr\ntorch.Tensor.fliplr(_input_tensor)\n'
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
import torch
input_tensor = torch.rand(2, 3, 4)
print(input_tensor)
output_tensor = input_tensor.fliplr(dim=2)
print(output_tensor)