'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.imag\ntorch.imag(input)\n'
import torch
input_data = torch.tensor([(1 + 2j), (3 + 4j), (5 + 6j)], dtype=torch.complex64)
print('The imaginary part of the tensor: {}'.format(torch.imag(input_data)))