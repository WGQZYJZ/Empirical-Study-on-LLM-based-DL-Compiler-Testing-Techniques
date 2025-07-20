input_data = torch.arange(1, 25, dtype=torch.float32).reshape(1, 1, 4, 6)
output = torch.nn.functional.unfold(input_data, kernel_size=(2, 2), padding=(0, 0), stride=(1, 1))