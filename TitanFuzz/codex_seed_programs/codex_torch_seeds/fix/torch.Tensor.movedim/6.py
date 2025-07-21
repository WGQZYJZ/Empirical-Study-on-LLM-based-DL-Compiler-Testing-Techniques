'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.movedim\ntorch.Tensor.movedim(_input_tensor, source, destination)\n'
import torch
tensor = torch.randn(3, 4, 5)
print(tensor.movedim(0, 2))