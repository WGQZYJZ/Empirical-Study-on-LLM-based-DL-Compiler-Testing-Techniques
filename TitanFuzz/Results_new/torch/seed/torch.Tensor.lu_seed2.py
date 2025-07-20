_input_tensor = torch.randn(3, 3)
lu_output = torch.Tensor.lu(_input_tensor, pivot=True, get_infos=False)