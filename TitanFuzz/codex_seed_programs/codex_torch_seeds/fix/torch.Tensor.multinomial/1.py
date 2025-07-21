'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.multinomial\ntorch.Tensor.multinomial(_input_tensor, num_samples, replacement=False, *, generator=None)\n'
import torch
input_tensor = torch.Tensor([[0.1, 0.2, 0.3, 0.4], [0.1, 0.2, 0.3, 0.4]])
output_tensor = torch.Tensor.multinomial(input_tensor, num_samples=2)
print(output_tensor)