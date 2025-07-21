'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.to\ntorch.Tensor.to(_input_tensor, *args, **kwargs)\n'
import torch
data = torch.rand(2, 3, 4)
device = torch.device('cuda:0')
data_cuda = data.to(device)
print('data_cuda = ', data_cuda)