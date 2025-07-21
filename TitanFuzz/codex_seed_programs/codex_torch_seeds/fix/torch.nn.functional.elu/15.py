'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
import torch.nn.functional as F
input_data = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
output_data = F.elu(input_data)
print(output_data)