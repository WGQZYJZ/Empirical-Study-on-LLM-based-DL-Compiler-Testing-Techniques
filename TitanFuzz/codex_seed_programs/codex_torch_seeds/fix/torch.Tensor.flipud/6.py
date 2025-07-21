'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.flipud\ntorch.Tensor.flipud(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_tensor)
flip_tensor = torch.Tensor.flipud(input_tensor)
print(flip_tensor)
fliplr_tensor = torch.Tensor.fliplr(input_tensor)
print(fliplr_tensor)