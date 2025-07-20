input_data = torch.randn(1, 1, 1, 1)
torch._assert((input_data.shape[0] == 1), 'Input data shape is not correct')