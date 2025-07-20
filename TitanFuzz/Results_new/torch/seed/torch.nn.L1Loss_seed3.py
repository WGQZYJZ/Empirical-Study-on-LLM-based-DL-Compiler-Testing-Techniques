input = torch.tensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype=torch.float32)
target = torch.tensor([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], dtype=torch.float32)
l1_loss = torch.nn.L1Loss()
loss = l1_loss(input, target)