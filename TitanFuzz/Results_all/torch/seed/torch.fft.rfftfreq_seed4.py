in_data = torch.randn(10, dtype=torch.float32)
out_data = torch.fft.rfftfreq(in_data.size(0))