"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.huber_loss\ntorch.nn.functional.huber_loss(input, target, reduction='mean', delta=1.0)\n"
import torch
input_data = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0])
target_data = torch.tensor([0.0, 0.0, 0.0, 0.0, 0.0])
print(torch.nn.functional.huber_loss(input_data, target_data, delta=1.0))
input_data = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0])
target_data = torch.tensor([1.0, 1.0, 1.0, 1.0, 1.0])
print(torch.nn.functional.huber_loss(input_data, target_data, delta=1.0))
input_data = torch.tensor([0.0, 1.0, 2.0, 3.0, 4.0])
target_data = torch.tensor([1.0, 1.0, 1.0, 1.0, 1.0])