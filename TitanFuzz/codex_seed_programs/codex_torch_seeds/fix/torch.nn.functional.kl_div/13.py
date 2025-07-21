"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
input_data = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], dtype=torch.float32)
target_data = torch.tensor([[0.1, 0.2, 0.3], [0.1, 0.2, 0.3]], dtype=torch.float32)
output_data = torch.nn.functional.kl_div(input_data, target_data, reduction='batchmean')
print(output_data)