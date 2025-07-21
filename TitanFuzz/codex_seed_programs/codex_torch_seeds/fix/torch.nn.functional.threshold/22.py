'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.threshold\ntorch.nn.functional.threshold(input, threshold, value, inplace=False)\n'
import torch
input_data = torch.tensor([[(- 1.0), (- 0.5), 0.0, 0.5, 1.0]])
print(input_data)
threshold = 0.0
value = 0.0
print(torch.nn.functional.threshold(input_data, threshold, value))