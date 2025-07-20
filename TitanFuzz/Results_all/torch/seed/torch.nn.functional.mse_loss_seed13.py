input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
target = torch.tensor([[2, 4, 6], [8, 10, 12]], dtype=torch.float32)
loss = torch.nn.functional.mse_loss(input_data, target)