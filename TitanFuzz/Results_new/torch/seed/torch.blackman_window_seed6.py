input_data = torch.linspace(0, 1, steps=10)
output = torch.blackman_window(input_data.size()[0])