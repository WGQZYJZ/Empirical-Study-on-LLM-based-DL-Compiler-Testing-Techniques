'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
from torch.utils.data import Subset
import torch
input_data = torch.randn(10)
output_data = Subset(input_data, [1, 2, 3])
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.TensorDataset\ntorch.utils.data.TensorDataset(data_tensor, target_tensor)\n'
import torch
from torch.utils.data import TensorDataset
import torch
data_tensor = torch.randn(10)
target_tensor = torch.randn(10)