data = torch.rand(2, 3)
dlpack = torch.utils.dlpack.to_dlpack(data)
data_np = np.array(dlpack)