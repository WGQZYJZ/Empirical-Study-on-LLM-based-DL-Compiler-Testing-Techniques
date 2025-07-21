"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.mse_loss\ntorch.nn.functional.mse_loss(input, target, size_average=None, reduce=None, reduction='mean')\n"
import torch
input_data = torch.tensor([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]])
target_data = torch.tensor([[0.0], [0.0], [1.0], [1.0]])
loss_function = torch.nn.MSELoss()
loss = loss_function(input_data, target_data)
print(loss)