'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
if True:
    input_data = torch.arange(1, 17).view(4, 4)
    print('Input data:\n', input_data)
    print('\nDiagonal elements: ', torch.diagonal(input_data))
    print('Diagonal elements, offset=1: ', torch.diagonal(input_data, offset=1))
    print('Diagonal elements, offset=-1: ', torch.diagonal(input_data, offset=(- 1)))
    print('Diagonal elements, offset=1, dim1=1, dim2=0: ', torch.diagonal(input_data, offset=1, dim1=1, dim2=0))