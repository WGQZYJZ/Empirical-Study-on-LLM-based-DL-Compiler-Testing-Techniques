'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sum_to_size\ntorch.Tensor.sum_to_size(_input_tensor, *size)\n'
import torch
input_tensor = torch.randint(low=0, high=10, size=(2, 3, 4, 5))
print('Input tensor: {}'.format(input_tensor))
sum_to_size_result = input_tensor.sum_to_size((2, 3, 4))
print('Result of sum_to_size: {}'.format(sum_to_size_result))