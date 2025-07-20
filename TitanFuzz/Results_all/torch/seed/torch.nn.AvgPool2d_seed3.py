input_data = torch.tensor([[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]], dtype=torch.float32)
avg_pool2d = torch.nn.AvgPool2d(kernel_size=3, stride=2, padding=1)
output_data = avg_pool2d(input_data)