'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
x = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], requires_grad=True)
y = torch.tensor([[10.0], [20.0]], requires_grad=True)
linear = torch.nn.Linear(3, 1)
linear.weight = torch.nn.Parameter(torch.tensor([[1.0, 2.0, 3.0]], requires_grad=True))
linear.bias = torch.nn.Parameter(torch.tensor([1.0], requires_grad=True))
pred = linear(x)
loss = torch.nn.functional.mse_loss(pred, y)
loss.backward()