"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.PoissonNLLLoss\ntorch.nn.PoissonNLLLoss(log_input=True, full=False, size_average=None, eps=1e-08, reduce=None, reduction='mean')\n"
import torch
x = torch.rand(10, 1)
y = torch.rand(10, 1)
loss = torch.nn.PoissonNLLLoss(reduction='none')(x, y)
print(loss)