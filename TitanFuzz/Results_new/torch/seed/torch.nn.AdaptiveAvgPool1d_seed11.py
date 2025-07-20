if True:
    input_data = torch.arange(1, 11, dtype=torch.float32).reshape(1, 1, 10)
    print('input_data:', input_data)
    avg_pool1d = torch.nn.AdaptiveAvgPool1d(3)
    output_data = avg_pool1d(input_data)
    print('output_data:', output_data)