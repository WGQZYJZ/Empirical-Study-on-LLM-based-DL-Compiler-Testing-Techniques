'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adadelta\ntorch.optim.Adadelta(params, lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)\n'
import torch
x = torch.tensor([1.0], requires_grad=True)
y = torch.tensor([2.0], requires_grad=True)
optimizer = torch.optim.Adadelta([x, y], lr=1.0, rho=0.9, eps=1e-06, weight_decay=0)
optimizer.step()
print(x, y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.optim.Adagrad\ntorch.optim.Adagrad(params, lr=0.01, lr_decay=0, weight_decay=0, initial_accumulator_value=0)\n'
import torch