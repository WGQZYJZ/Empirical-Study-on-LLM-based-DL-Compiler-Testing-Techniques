

# Initializing the model
m  = torch.nn.MultiheadAttention(embed_dim=10, num_heads=5)

# Inputs to the model
q = torch.randn(64, 32, 10) # Tensor of shape (batch size, sequence length, embedding dimension)
k = torch.randn(64, 32, 10) # Tensor of shape (batch size, sequence length, embedding dimension)
v = torch.randn(64, 32, 10) # Tensor of shape (batch size, sequence length, embedding dimension)

__outputs__  = m(q, k, v)

