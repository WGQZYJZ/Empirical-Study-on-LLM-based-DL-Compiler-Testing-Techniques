x = torch.rand(2, 3)
dlpack_tensor = torch.utils.dlpack.to_dlpack(x)