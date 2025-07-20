input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=torch.float)
target_data = torch.tensor([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=torch.float)
loss_fn = torch.nn.SoftMarginLoss()
loss = loss_fn(input_data, target_data)