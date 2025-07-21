'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
import torch
input_data = torch.tensor([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]])
padding_1 = torch.nn.ZeroPad2d(padding=(1, 1, 1, 1))
padding_2 = torch.nn.ZeroPad2d(padding=(2, 2, 2, 2))
padding_3 = torch.nn.ZeroPad2d(padding=(3, 3, 3, 3))
output_data_1 = padding_1(input_data)
output_data_2 = padding_2(input_data)
output_data_3 = padding_3(input_data)
print('Input data:')
print(input_data)
print