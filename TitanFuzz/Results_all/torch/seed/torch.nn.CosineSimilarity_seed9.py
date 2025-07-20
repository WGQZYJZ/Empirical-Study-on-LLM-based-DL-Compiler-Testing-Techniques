input_data = Variable(torch.randn(3, 5))
cos = torch.nn.CosineSimilarity(dim=1, eps=1e-08)
output = cos(input_data, input_data)