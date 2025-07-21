'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.futures.Future\ntorch.futures.Future(*, devices=None)\n'
import torch
if True:
    print('PyTorch version: ', torch.__version__)
    input_data = torch.rand(10, 10)
    print('input_data: ', input_data)
    future = torch.futures.Future()