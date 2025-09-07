

# Initializing the model
m  = ScaledDotProductAttention()

# Inputs to the model
q1   = torch.randn(32, 80, 64) # query tensor of shape (batch size, sequence length, embedding dimension)
k1   = torch.randn(32, 80, 64) # key tensor of shape (batch size, sequence length, embedding dimension)
v1   = torch.randn(32, 80, 64) # value tensor of shape (batch size, sequence length, embedding dimension)

