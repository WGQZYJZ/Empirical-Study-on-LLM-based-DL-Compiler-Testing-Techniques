input_data = Variable(torch.randn(2, 3))
output_data = torch.nn.functional.gumbel_softmax(input_data)