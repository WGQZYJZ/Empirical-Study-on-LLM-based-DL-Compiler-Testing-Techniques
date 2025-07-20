input = torch.randn(1, 1, 32, 32)
torch.random.manual_seed(2)
conv2d = torch.nn.Conv2d(1, 1, 3, bias=False)
torch.nn.init.kaiming_uniform_(conv2d.weight)
output = torch.nn.functional.conv2d(input, conv2d.weight)
torch.nn.init.kaiming_uniform_(conv2d.weight)
output = torch.nn.functional.conv2d