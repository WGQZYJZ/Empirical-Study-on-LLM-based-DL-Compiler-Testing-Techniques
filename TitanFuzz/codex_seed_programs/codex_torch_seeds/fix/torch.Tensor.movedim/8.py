'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.movedim\ntorch.Tensor.movedim(_input_tensor, source, destination)\n'
import torch
data_tensor = torch.rand(4, 3, 2)
print(data_tensor)
moved_tensor = data_tensor.movedim(0, 2)
print(moved_tensor)