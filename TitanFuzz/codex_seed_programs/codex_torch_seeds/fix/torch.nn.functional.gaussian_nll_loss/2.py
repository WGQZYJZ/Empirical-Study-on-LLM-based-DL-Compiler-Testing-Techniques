"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gaussian_nll_loss\ntorch.nn.functional.gaussian_nll_loss(input, target, var, full=False, eps=1e-06, reduction='mean')\n"
import torch
import torch
input_data = torch.tensor([[0.5, 0.5, 0.5, 0.5]])
target_data = torch.tensor([[0.5, 0.5, 0.5, 0.5]])
var_data = torch.tensor([[0.5, 0.5, 0.5, 0.5]])
loss = torch.nn.functional.gaussian_nll_loss(input_data, target_data, var_data)
print(loss)
loss = torch.nn.functional.gaussian_nll_loss(input_data, target_data, var_data, reduction='none')
print(loss)
loss = torch.nn.functional.gaussian_nll_loss(input_data, target_data, var_data, full=True)
print(loss)