'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.swapdims\ntorch.swapdims(input, dim0, dim1)\n'
import torch
if True:
    input = torch.randint(low=0, high=10, size=(2, 3, 4))
    print('Input: \n', input)
    output = torch.swapdims(input, dim0=0, dim1=2)
    print('Output: \n', output)