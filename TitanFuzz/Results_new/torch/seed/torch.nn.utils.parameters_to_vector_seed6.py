input_data = [torch.randn(1, 3, 224, 224), torch.randn(1, 3, 224, 224)]
vector = torch.nn.utils.parameters_to_vector(input_data)