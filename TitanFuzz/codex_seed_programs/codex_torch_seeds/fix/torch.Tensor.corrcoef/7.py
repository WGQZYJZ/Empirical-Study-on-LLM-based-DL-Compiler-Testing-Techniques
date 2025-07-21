'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.corrcoef\ntorch.Tensor.corrcoef(_input_tensor)\n'
import torch
data = torch.randn(2, 5)
corrcoef = data.corrcoef()
print('The input data is:')
print(data)
print('The corrcoef is:')
print(corrcoef)