input_data = torch.randn(2, 3, requires_grad=True)
output_data = torch.nn.functional.log_softmax(input_data, dim=1)