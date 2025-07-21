'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.Subset\ntorch.utils.data.Subset(dataset, indices)\n'
import torch
import numpy as np
print(torch.__version__)
input_data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(input_data)
subset_indices = [0, 2]
subset = torch.utils.data.Subset(input_data, subset_indices)
print(subset)