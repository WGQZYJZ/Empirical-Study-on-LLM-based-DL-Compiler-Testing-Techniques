input = torch.arange(1, 7, dtype=torch.float).view(1, 1, 2, 3)
unfold = torch.nn.Unfold(kernel_size=(2, 2))
output = unfold(input)