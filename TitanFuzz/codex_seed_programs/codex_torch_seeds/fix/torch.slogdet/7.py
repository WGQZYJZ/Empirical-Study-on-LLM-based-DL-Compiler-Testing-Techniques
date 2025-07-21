'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.slogdet\ntorch.slogdet(input)\n'
import torch
input_data = torch.randn(3, 3)
(sign, logdet) = torch.slogdet(input_data)
print('Sign: ', sign)
print('Logdet: ', logdet)