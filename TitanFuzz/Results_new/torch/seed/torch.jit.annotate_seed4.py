input_data = torch.randn(5, 3)
input_data_type = torch.jit.annotate(torch.Tensor, input_data)