'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reshape\ntorch.Tensor.reshape(_input_tensor, *shape)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('The input tensor is: \n{}'.format(input_tensor))
reshaped_tensor = input_tensor.reshape(2, 6)
print('The reshaped tensor is: \n{}'.format(reshaped_tensor))