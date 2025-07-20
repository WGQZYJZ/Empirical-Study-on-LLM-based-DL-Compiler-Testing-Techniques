input = torch.randn(2, 3, 4)
output = torch.fft.fft2(input, s=None, dim=((- 2), (- 1)), norm=None, out=None)
input_np = input.numpy()
output_np = np.fft.fft2(input_np)