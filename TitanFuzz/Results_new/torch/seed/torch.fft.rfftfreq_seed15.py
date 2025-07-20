N = 10
x = torch.randn(N)
freq = torch.fft.rfftfreq(N, d=1.0)
freq2 = torch.fft.rfftfreq(N, d=1.0, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)
freq3 = torch.fft.rfftfreq(N, d=1.0, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)