'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.get_worker_info\ntorch.utils.data.get_worker_info()\n'
import torch
import torch.utils.data
input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dataset = torch.utils.data.TensorDataset(torch.tensor(input_data))
data_loader = torch.utils.data.DataLoader(dataset)
worker_info = torch.utils.data.get_worker_info()
print(worker_info)