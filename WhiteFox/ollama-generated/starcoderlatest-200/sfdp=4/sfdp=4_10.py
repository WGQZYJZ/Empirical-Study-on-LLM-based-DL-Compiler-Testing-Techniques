

# Initializing the model
m = QueryKeyAttentionModel()

# Inputs to the model
query = torch.randn(16, 32, 16, 16) # Batch size: 16; Number of heads: 8; Sequence length: 16; The shape of each head is (16, 32, 4, 4). Each tensor has one element per pixel.
key = torch.randn(16, 32, 8, 16) # Batch size: 16; Number of heads: 8; Sequence length: 16; The shape of each head is (8, 32, 4, 4). Each tensor has one element per pixel.
value = torch.randn(16, 32, 64, 16) # Batch size: 16; Number of heads: 8; Sequence length: 16; The shape of each head is (64, 32, 4, 4). Each tensor has one element per pixel.
attn_mask = torch.randn(16, 32, 64, 64) # Batch size: 16; Number of heads: 8; Sequence length: 64; The shape of each head is (64, 32, 1, 1). Each tensor has one element per pixel.
