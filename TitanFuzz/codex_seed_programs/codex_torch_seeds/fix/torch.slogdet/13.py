'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.slogdet\ntorch.slogdet(input)\n'
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
(sign, logdet) = torch.slogdet(input_data)
print('sign: ', sign)
print('logdet: ', logdet)