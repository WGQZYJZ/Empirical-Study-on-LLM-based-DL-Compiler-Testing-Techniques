"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
import torch
input = torch.rand(3, requires_grad=True)
input_log_softmax = torch.nn.functional.log_softmax(input, dim=0)
target = torch.rand(3)
target_log_softmax = torch.nn.functional.log_softmax(target, dim=0)
loss = torch.nn.functional.kl_div(input_log_softmax, target_log_softmax, reduction='batchmean')
print(loss)