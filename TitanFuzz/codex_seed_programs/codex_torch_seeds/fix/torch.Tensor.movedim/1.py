'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.movedim\ntorch.Tensor.movedim(_input_tensor, source, destination)\n'
import torch
input_tensor = torch.randn(2, 3, 4, 5)
print(input_tensor)
output_tensor = input_tensor.movedim(0, 1)
print(output_tensor)