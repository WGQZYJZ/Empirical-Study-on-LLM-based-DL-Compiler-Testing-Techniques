'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
input_tensor = torch.randint(low=0, high=2, size=(3, 3), dtype=torch.int32)
print('Input data:\n', input_tensor)
output_tensor = torch.Tensor.bitwise_not_(input_tensor)
print('Output data:\n', output_tensor)
output_tensor = torch.bitwise_not(input_tensor)
print('Output data:\n', output_tensor)