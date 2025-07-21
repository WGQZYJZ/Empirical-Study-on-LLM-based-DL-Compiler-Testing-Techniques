'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.normalize\ntorch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)\n'
import torch
import torch.nn.functional as F
input = torch.randn(2, 3)
normalized_input = F.normalize(input, p=2.0, dim=1, eps=1e-12)
print('input:', input)
print('normalized_input:', normalized_input)
if torch.allclose(normalized_input, torch.tensor([[0.6, 0.8, 0.0], [0.4472, 0.8944, 0.0]])):
    print('Congratulations! You have finished this task!')
else:
    print('Please check your code and try again!')