input_data = torch.randn(2, 3)
torch._assert((input_data.dim() == 2), 'input data should be 2D')