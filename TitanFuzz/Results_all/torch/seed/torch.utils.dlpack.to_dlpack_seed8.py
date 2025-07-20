input_data = torch.randn(2, 3)
dlpack_data = torch.utils.dlpack.to_dlpack(input_data)