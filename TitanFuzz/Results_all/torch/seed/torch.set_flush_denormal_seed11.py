x = torch.tensor([1e-323], dtype=torch.float32)
torch.set_flush_denormal(True)
torch.set_flush_denormal(False)