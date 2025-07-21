"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
input_data = torch.Tensor([[1, 2, 3], [4, 5, 6]])
target_data = torch.Tensor([[1, 1, 1], [1, 1, 1]])
loss = torch.nn.KLDivLoss(reduction='batchmean')
loss_output = loss(input_data, target_data)
print(loss_output)