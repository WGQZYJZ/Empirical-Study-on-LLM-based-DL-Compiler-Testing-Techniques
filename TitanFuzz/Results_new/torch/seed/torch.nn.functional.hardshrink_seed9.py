x = torch.rand(5, 5)
shrinked = torch.nn.functional.hardshrink(x)