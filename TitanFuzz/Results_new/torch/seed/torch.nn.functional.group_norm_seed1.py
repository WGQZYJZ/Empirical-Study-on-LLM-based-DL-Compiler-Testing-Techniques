input = torch.randn(4, 4, 4, 4)
num_groups = 2
output = torch.nn.functional.group_norm(input, num_groups)