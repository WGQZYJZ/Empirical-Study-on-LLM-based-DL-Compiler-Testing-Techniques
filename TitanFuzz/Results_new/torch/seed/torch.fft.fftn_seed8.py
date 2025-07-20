input = torch.randn(1, 3, 4, 5)
out = torch.fft.fftn(input, s=None, dim=None, norm=None, out=None)
out_np = out.numpy()