input_data = torch.randn(1, 5)
target_data = torch.randn(1, 5)
loss = torch.nn.functional.l1_loss(input_data, target_data)