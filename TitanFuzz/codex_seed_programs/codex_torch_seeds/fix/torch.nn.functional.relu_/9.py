'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.relu_\ntorch.nn.functional.relu_(input)\n'
import torch
import torch
input_data = torch.tensor([(- 1.0), 1.0, 3.0, 5.0])
output_data = torch.nn.functional.relu_(input_data)
print('input_data:', input_data)
print('output_data:', output_data)
assert torch.equal(output_data, torch.tensor([0.0, 1.0, 3.0, 5.0]))
print('Well done!')