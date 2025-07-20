tensor = torch.ones(2, 3)
dlpack = torch.utils.dlpack.to_dlpack(tensor)
tensor = torch.utils.dlpack.from_dlpack(dlpack)