'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multinomial\ntorch.Tensor.multinomial(_input_tensor, num_samples, replacement=False, *, generator=None)\n'
import torch
input_tensor = torch.rand(10, 10)
output_tensor = input_tensor.multinomial(5)
print(input_tensor)
print(output_tensor)