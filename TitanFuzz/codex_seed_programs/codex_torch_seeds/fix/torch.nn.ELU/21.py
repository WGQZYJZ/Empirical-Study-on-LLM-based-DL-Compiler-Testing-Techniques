'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
input_data = torch.tensor([(- 1), 0, 1, 2], dtype=torch.float32)
print('Input data: ', input_data)
elu = torch.nn.ELU(alpha=1.0, inplace=False)
output_data = elu(input_data)
print('Output data: ', output_data)