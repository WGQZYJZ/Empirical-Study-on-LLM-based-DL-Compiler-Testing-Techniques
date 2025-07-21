'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.acosh\ntorch.Tensor.acosh(_input_tensor)\n'
import torch
input_tensor = torch.tensor([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
output_tensor = input_tensor.acosh()
print('input_tensor: ', input_tensor)
print('output_tensor: ', output_tensor)