'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softshrink\ntorch.nn.Softshrink(lambd=0.5)\n'
import torch
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
softshrink = torch.nn.Softshrink(lambd=0.5)
print(softshrink(input_data))