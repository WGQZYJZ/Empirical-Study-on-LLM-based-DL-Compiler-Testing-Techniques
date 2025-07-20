tensor = torch.rand(2, 3)
dlpack = torch.utils.dlpack.to_dlpack(tensor)