'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.copysign\ntorch.Tensor.copysign(_input_tensor, other)\n'
import torch
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
other = torch.tensor([1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1), 1, (- 1)])
output_tensor = input_tensor.copysign(other)
print('Output tensor: ', output_tensor)