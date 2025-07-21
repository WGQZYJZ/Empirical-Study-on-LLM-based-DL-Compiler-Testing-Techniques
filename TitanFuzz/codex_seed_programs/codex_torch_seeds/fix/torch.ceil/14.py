'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ceil\ntorch.ceil(input, *, out=None)\n'
import torch
inputData = torch.tensor([0.1, 0.5, 0.7, 1.2, (- 0.1), (- 0.5), (- 0.7), (- 1.2)])
ceilData = torch.ceil(inputData)
print('Input data:\n', inputData)
print('Ceil data:\n', ceilData)