'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input_data = torch.tensor([[1, (- 1), 0], [2, (- 2), 0], [3, (- 3), 0]])
output_data = torch.positive(input_data)
print('Input data:')
print(input_data)
print('Output data:')
print(output_data)