input_data = torch.tensor(data=[[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float)
mse_loss = torch.nn.MSELoss()
loss = mse_loss(input_data, input_data)