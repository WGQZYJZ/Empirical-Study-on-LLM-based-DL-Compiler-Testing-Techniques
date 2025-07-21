'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
input = torch.randn(3, 3)
print(input)
print(torch.nn.functional.layer_norm(input, [3]))
print(torch.nn.functional.layer_norm(input, [3], weight=torch.tensor([1.0, 2.0, 3.0]), bias=torch.tensor([0.1, 0.2, 0.3])))
print(torch.nn.functional.layer_norm(input, [3], weight=torch.tensor([1.0, 2.0, 3.0]), bias=torch.tensor([0.1, 0.2, 0.3]), eps=1e-06))