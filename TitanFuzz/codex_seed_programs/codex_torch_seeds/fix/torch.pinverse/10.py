'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.pinverse\ntorch.pinverse(input, rcond=1e-15)\n'
import torch
if True:
    print('Task 1: import PyTorch')
    print('PyTorch version: ', torch.__version__)
    print('\nTask 2: Generate input data')
    input_data = torch.randn(3, 5)
    print('input_data: ', input_data)
    print('\nTask 3: Call the API torch.pinverse')
    pinv_data = torch.pinverse(input_data)
    print('pinv_data: ', pinv_data)