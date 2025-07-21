'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.geqrf\ntorch.Tensor.geqrf(_input_tensor)\n'
import torch
input_tensor = torch.randn(4, 4)
out = torch.Tensor.geqrf(input_tensor)
print(out)