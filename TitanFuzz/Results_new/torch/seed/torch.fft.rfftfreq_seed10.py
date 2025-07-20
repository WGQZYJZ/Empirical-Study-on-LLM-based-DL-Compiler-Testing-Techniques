t = torch.arange(0, 10, 0.01)
x = torch.sin(t)
freq = torch.fft.rfftfreq(len(t), d=0.01)