'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multinomial\ntorch.Tensor.multinomial(_input_tensor, num_samples, replacement=False, *, generator=None)\n'
import torch
input_tensor = torch.rand(2, 3)
print(input_tensor)
output_tensor = torch.Tensor.multinomial(input_tensor, 5, replacement=False)
print(output_tensor)