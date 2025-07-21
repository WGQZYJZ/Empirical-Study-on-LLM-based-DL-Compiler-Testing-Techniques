'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu_\ntorch.nn.functional.elu_(input, alpha=1.)\n'
import torch
input_data = torch.tensor([[(- 1), 1, (- 2), 2, (- 3), 3]], dtype=torch.float32)
print(torch.nn.functional.elu(input_data))
print(torch.nn.functional.elu_(input_data))