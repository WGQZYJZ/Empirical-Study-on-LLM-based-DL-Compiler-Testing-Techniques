input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
max_val_1 = torch.amax(input_data)
max_val_2 = torch.amax(input_data, dim=1)
max_val_3 = torch.amax(input_data, dim=1, keepdim=True)