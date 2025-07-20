input_data = Variable(torch.Tensor([[1, 2, 3], [4, 5, 6]]))
target_data = Variable(torch.Tensor([[0.9, 1.9, 3.1], [3.9, 5.1, 6.1]]))
smooth_l1_loss = torch.nn.SmoothL1Loss()
loss = smooth_l1_loss(input_data, target_data)