"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PoissonNLLLoss\ntorch.nn.PoissonNLLLoss(log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
import torch
input = torch.randn(3, 5, requires_grad=True)
target = torch.empty(3, 5).random_(2)
loss = torch.nn.PoissonNLLLoss()
output = loss(input, target)
output.backward()