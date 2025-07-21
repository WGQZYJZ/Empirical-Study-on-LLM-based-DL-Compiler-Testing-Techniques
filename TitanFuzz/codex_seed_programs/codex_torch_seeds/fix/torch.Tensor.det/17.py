'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.det\ntorch.Tensor.det(_input_tensor)\n'
import torch
print('\nTask 1:')
print(torch.__version__)
print('\nTask 2:')
input_tensor = torch.tensor([[2, 3], [4, 5]])
print(input_tensor)
print('\nTask 3:')
print(input_tensor.det())