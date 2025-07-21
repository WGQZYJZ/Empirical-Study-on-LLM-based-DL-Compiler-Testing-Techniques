'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.threshold\ntorch.nn.functional.threshold(input, threshold, value, inplace=False)\n'
import torch
import torch
input_data = torch.tensor([[(- 1), (- 0.5), 0, 0.5, 1]])
output_data = torch.nn.functional.threshold(input_data, 0.0, 0.0)
print(input_data)
print(output_data)
output_data = torch.nn.functional.threshold(input_data, 0.0, 0.0, inplace=True)
print(input_data)
print(output_data)