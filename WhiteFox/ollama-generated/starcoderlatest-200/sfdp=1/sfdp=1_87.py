

# Initializing the model
m = Model()


# Inputs to the model
query = torch.randn(4, 3, 64, 64)
key   = torch.randn(4, 3, 64, 64)
value = torch.randn(4, 8, 64, 64)

