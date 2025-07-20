input_data = torch.randn(1, 1, 3, 3)
target_data = torch.randn(1, 1, 3, 3)
loss = torch.nn.functional.smooth_l1_loss(input_data, target_data)