input = torch.randn(5)
output = torch.nn.functional.relu(input)
input = torch.randn(5)
output = torch.nn.functional.relu_(input)
input = torch.randn(5)
output = torch.nn.functional.leaky_relu(input)
input = torch