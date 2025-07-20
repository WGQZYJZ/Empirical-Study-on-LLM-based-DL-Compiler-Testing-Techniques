input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dataset = torch.utils.data.TensorDataset(torch.tensor(input_data))
data_loader = torch.utils.data.DataLoader(dataset)
worker_info = torch.utils.data.get_worker_info()