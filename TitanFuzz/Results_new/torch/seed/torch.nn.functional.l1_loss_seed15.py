input = torch.tensor([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
target = torch.tensor([[1.0, 1.0, 1.0], [1.0, 1.0, 1.0]])
l1_loss = torch.nn.functional.l1_loss(input, target)