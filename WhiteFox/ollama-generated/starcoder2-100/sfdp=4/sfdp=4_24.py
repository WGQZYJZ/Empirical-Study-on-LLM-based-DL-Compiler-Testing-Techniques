# Initializing the model
sa_attn  = ScaledDotProductAttention()


# Inputs to the model
q  = torch.randn(32, 10, 8)
k = q  # Using the same query tensor as key. This is for testing.
v  = torch.randn(32, 10, 4)
m  = torch.ones(1, k.size(-2), k.size(-1))  # Attention mask to avoid attention to self-attention.


