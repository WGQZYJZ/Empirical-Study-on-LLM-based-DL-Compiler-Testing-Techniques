'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.AbsTransform\ntorch.distributions.transforms.AbsTransform(cache_size=0)\n'
import torch
input_data = torch.tensor([(- 2.0), (- 1.0), 0.0, 1.0, 2.0])
print('Input data: ', input_data)
abs_transform = torch.distributions.transforms.AbsTransform()
output_data = abs_transform(input_data)
print('Output data: ', output_data)