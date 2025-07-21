'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.movedim\ntorch.Tensor.movedim(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.rand(3, 4, 5)
print(torch.Tensor.movedim(input_tensor, 0, 2))