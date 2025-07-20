input = torch.randn(1, 1)
target = torch.randn(1, 1)
loss = torch.nn.functional.mse_loss(input, target)