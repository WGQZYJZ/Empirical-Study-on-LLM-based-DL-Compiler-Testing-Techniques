'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.device\ntorch.Tensor.device(_input_tensor, )\n'
import torch
x = torch.tensor([1, 2, 3])
device = 'cpu'
output = x.device(device)
print('output: ', output)