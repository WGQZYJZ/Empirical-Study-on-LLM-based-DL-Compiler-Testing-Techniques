input_data = Variable(torch.randn(3, 5))
target_data = Variable(torch.randn(3, 5))
loss = torch.nn.functional.smooth_l1_loss(input_data, target_data)