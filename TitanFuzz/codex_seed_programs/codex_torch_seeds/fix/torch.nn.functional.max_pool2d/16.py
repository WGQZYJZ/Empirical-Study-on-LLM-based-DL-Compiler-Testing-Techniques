'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_pool2d\ntorch.nn.functional.max_pool2d(input, kernel_size, stride=None, padding=0, dilation=1, return_indices=False, ceil_mode=False)\n'
import torch
input_data = torch.tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]]], dtype=torch.float32)
output_data = torch.nn.functional.max_pool2d(input_data, kernel_size=[2, 2], stride=[2, 2], padding=[0, 0])
print('\ninput_data = \n', input_data)
print('\noutput_data = \n', output_data)