'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.resolve_neg\ntorch.Tensor.resolve_neg(_input_tensor)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import numpy as np
import torch
input_data = np.array([[1, 2, 3], [4, 5, 6]])
input_data = torch.from_numpy(input_data)
output_data = input_data.resolve_neg()
print(output_data)