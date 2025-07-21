'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.one_hot\ntorch.nn.functional.one_hot(tensor, num_classes=-1)\n'
import torch
import numpy as np
import torch
input_data = torch.tensor([[0, 1, 2, 3, 4], [0, 1, 2, 3, 4]])
output_data = torch.nn.functional.one_hot(input_data, num_classes=5)
print(output_data)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softmax\ntorch.nn.functional.softmax(input, dim=-1, dtype=None)\n'
import torch
import numpy as np
import torch