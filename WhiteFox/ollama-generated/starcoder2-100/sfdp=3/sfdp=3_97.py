# Initializing the model
m = Model()


# Inputs to the model
query1, key1, value2 = torch.randn(50, 768), torch.randn(50, 32*32, 768), torch.randn(32*32, 49)


