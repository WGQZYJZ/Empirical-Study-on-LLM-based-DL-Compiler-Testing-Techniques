if True:
    input_data = torch.randn(2, 3, 4)
    print('input_data: ', input_data)
    output_data = torch.fft.ifft2(input_data)
    print('output_data: ', output_data)