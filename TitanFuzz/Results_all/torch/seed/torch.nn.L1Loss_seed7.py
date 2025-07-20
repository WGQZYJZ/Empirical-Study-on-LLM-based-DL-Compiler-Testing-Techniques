input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
target_data = torch.tensor([[0, 1, 0], [1, 1, 0]], dtype=torch.float32)
loss_fn = torch.nn.L1Loss()
loss = loss_fn(input_data, target_data)