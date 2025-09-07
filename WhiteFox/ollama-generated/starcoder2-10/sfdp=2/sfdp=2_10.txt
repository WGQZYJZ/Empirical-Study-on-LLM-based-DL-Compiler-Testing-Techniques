

# Initializing the model
model  = torch.nn.Transformer()

# Inputs to the model
query, key, value = torch.randn(1024, 3, 512), torch.randn(1024, 3, 512), torch.randn(1024, 3, 512)

