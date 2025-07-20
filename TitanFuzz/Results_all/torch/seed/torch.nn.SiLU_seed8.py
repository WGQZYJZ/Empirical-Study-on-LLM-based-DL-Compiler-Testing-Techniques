input_data = torch.randn(2, 3)
silu = torch.nn.SiLU(inplace=False)
output = silu(input_data)