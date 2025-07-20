input_tensor = torch.randn(4, 4, 4, 4)
start = time.time()
output_tensor = torch.fft.irfftn(input_tensor, s=None, dim=None, norm=None, out=None)
end = time.time()