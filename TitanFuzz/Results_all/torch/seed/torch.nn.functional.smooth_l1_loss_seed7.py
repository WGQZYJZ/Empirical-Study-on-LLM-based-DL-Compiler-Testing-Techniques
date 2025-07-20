input = torch.randn((3, 3))
target = torch.randn((3, 3))
loss = torch.nn.functional.smooth_l1_loss(input, target)