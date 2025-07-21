'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.utils.data.get_worker_info\ntorch.utils.data.get_worker_info()\n'
import torch
import torch.utils.data as data
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_loader = data.DataLoader(dataset=data_list, batch_size=4, shuffle=True)
for (i_batch, batch_data) in enumerate(data_loader):
    print(i_batch, batch_data)
    if (i_batch == 2):
        break
print(torch.utils.data.get_worker_info())