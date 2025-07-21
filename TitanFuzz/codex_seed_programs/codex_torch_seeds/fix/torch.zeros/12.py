'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.zeros\ntorch.zeros(*size, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
output = torch.zeros(input_data.size())
print('The output tensor: ', output)
print('The shape of the output tensor: ', output.shape)