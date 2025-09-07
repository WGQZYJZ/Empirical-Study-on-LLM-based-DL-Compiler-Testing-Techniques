

# Initializing the model
m  = torch.nn.MultiheadAttention(embed_dim=64, num_heads=8)

# Inputs to the model
input1  = torch.randn(32, 9000, 768)
input2  = torch.randn(32, 500, 768)

