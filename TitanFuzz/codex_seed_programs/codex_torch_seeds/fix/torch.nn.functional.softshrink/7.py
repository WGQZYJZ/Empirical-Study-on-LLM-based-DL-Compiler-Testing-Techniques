'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softshrink\ntorch.nn.functional.softshrink(input, lambd=0.5)\n'
import torch
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
output = torch.nn.functional.softshrink(input_data, lambd=0.5)
print('input: ', input_data)
print('output: ', output)