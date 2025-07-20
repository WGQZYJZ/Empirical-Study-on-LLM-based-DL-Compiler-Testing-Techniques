parameters = [torch.randn(3, 4), torch.randn(5, 6), torch.randn(2, 3)]
vector = torch.nn.utils.parameters_to_vector(parameters)