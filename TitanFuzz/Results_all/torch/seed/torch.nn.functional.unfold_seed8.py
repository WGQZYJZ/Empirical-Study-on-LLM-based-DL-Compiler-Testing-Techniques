input_data = torch.arange(0, 9, dtype=torch.float32).reshape(1, 1, 3, 3)
output = torch.nn.functional.unfold(input_data, kernel_size=(2, 2), dilation=1, padding=0, stride=1)
output = torch.nn.functional.fold(output, output_size=(3, 3), kernel_size=(2, 2), dilation=1, padding=0, stride=1)