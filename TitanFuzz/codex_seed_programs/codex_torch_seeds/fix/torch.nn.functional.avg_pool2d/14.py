'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.avg_pool2d\ntorch.nn.functional.avg_pool2d(input, kernel_size, stride=None, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)\n'
import torch
input_data = torch.tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[11, 12, 13], [14, 15, 16], [17, 18, 19]]], [[[21, 22, 23], [24, 25, 26], [27, 28, 29]], [[31, 32, 33], [34, 35, 36], [37, 38, 39]]]])
print('input_data:')
print(input_data)
output_data = torch.nn.functional.avg_pool2d(input_data, kernel_size=2, stride=2)
print('output_data:')