input_data = torch.randn(1, 1, 4, 4)
unfold_data = torch.nn.Unfold(kernel_size=(2, 2))