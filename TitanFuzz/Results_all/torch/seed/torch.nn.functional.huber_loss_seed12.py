input_data = torch.randn(10, 5)
target_data = torch.randn(10, 5)
loss = torch.nn.functional.huber_loss(input_data, target_data, reduction='mean', delta=1.0)