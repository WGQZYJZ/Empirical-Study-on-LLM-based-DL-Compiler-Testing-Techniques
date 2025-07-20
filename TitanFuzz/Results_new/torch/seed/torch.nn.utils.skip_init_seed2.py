input_data = torch.randn(1, 1, 2, 2)
torch.nn.utils.skip_init(nn.Conv2d, *(1, 1, 2, 2))