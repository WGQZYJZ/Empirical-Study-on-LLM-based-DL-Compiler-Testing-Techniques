input = torch.randn(1, 16, 4, 4, 4)
torch.nn.functional.dropout3d(input, p=0.5, training=True, inplace=False)