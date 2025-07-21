'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj\ntorch.conj(input)\n'
import torch
if True:
    input_data = torch.randn(4, 4)
    print('Input data: ', input_data)
    output_data = torch.conj(input_data)
    print('Output data: ', output_data)