input = torch.Tensor([[1, 2, 3], [4, 5, 6]])
target = torch.Tensor([[2, 4, 6], [8, 10, 12]])
loss = torch.nn.SmoothL1Loss()
loss_value = loss(input, target)