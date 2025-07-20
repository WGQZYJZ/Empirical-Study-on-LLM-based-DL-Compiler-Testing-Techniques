input_data = torch.randn(3, 3)
norm_l2_dim_0_keepdim = torch.norm(input_data, p=2, dim=0, keepdim=True)