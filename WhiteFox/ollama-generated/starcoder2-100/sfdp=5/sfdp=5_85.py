
# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 327680, 5)
key   = torch.randn(1, 327680, 5)
value = torch.randn(1, 327680, 496)
attn_mask = torch.randn(1, 327680, 327680).fill_(float("-inf")).masked_fill_(mask == 0, float("nan")) # Attention mask of size (batch, sequence length query, sequence length key), with 1 for padded elements and -inf otherwise
dropout_p = torch.rand(1) * 0.5 + 0.2  # Random dropout probability in the range [0.3..0.8]
__output__  = m(query, key, value, attn_mask, dropout_p)

