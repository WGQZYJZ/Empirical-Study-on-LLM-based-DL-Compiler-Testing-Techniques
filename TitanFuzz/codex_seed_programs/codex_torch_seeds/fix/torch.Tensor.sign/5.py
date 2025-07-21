'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sign\ntorch.Tensor.sign(_input_tensor)\n'
import torch
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data:')
print(input_tensor)
print('\nOutput data:')
print(input_tensor.sign())