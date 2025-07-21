'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.threshold\ntorch.nn.functional.threshold(input, threshold, value, inplace=False)\n'
import torch
input_data = torch.randn(4, 4)
print('Input data: ', input_data)
threshold_value = 0.5
output_data = torch.nn.functional.threshold(input_data, threshold_value, 0)
print('Output data: ', output_data)