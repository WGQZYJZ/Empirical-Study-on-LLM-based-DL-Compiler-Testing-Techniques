"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.weight_norm\ntorch.nn.utils.weight_norm(module, name='weight', dim=0)\n"
import torch
from torch.nn.utils import weight_norm
input_data = torch.randn(1, 2, 3)
import torch
input_data = torch.randn(1, 2, 3)
weight_norm(torch.nn.Conv1d(2, 3, 3))(input_data)
weight_norm(torch.nn.Conv1d(2, 3, 3), dim=1)(input_data)
weight_norm(torch.nn.Conv1d(2, 3, 3), name='weight', dim=1)(input_data)
weight_norm(torch.nn.Conv1d(2, 3, 3), dim=1, name='weight')(input_data)