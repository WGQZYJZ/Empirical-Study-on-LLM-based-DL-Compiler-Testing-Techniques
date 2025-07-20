my_input = torch.randn(4, 3, 32, 32)
my_input = torch.randn(4, 3, 32, 32)
my_output = torch.nn.functional.pad(my_input, (1, 1, 1, 1))