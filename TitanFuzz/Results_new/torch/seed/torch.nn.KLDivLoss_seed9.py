input_data = Variable(torch.randn(5, 10))
target_data = Variable(torch.randn(5, 10))
loss_fn = torch.nn.KLDivLoss()
loss = loss_fn(input_data, target_data)