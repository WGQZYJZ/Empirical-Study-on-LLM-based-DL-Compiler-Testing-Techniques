input_data = torch.rand(10)
torch._assert((input_data.dim() == 1), 'input_data is not 1-dimensional')