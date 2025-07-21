'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.get_worker_info\ntorch.utils.data.get_worker_info()\n'
import torch
import numpy as np
x_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], dtype=np.float32)
y_data = np.array([[0], [1], [2]], dtype=np.float32)
print(torch.utils.data.get_worker_info())
print(torch.utils.data.get_worker_info())