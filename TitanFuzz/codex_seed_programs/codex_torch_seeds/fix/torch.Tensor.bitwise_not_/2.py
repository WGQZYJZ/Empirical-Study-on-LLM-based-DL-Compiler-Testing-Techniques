'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.bitwise_not_\ntorch.Tensor.bitwise_not_(_input_tensor)\n'
import torch
input_data = torch.randint(low=0, high=2, size=(1, 5), dtype=torch.uint8)
print('Input data:\n{}'.format(input_data))
output_data = torch.Tensor.bitwise_not_(input_data)
print('Output data:\n{}'.format(output_data))