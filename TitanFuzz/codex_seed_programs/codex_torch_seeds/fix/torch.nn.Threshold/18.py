'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Threshold\ntorch.nn.Threshold(threshold, value, inplace=False)\n'
import torch
input_data = torch.randn(2, 3)
print('Input data:\n{}'.format(input_data))
threshold_value = 0.5
threshold_module = torch.nn.Threshold(threshold_value, 0)
output_data = threshold_module(input_data)
print('Output data:\n{}'.format(output_data))