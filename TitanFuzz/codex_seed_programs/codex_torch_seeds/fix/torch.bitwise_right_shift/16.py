'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.bitwise_right_shift\ntorch.bitwise_right_shift(input, other, *, out=None)\n'
import torch
if True:
    input = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
    other = torch.randint(low=0, high=10, size=(3, 3), dtype=torch.int32)
    print('Input: ', input)
    print('Other: ', other)
    output = torch.bitwise_right_shift(input, other)
    print('Output: ', output)