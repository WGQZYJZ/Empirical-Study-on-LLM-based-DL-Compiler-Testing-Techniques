input_data = torch.randn(1, 2, 3)
strided_data = torch.empty_strided(size=[1, 2, 3], stride=[3, 1, 1])