input_data = torch.tensor([[[1, 2, 3, 4, 5, 6]]])
avg_pool1d = torch.nn.AvgPool1d(kernel_size=3, stride=1, padding=0, ceil_mode=False, count_include_pad=True)
output = avg_pool1d.forward(input_data)