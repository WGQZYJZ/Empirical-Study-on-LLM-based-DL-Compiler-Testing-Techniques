
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=64, num_heads=8)
 
    def forward(self, x1, x2, mask1, mask2):
        k, v, attn_weights = self.attn(x1, x2, x2, key_padding_mask=mask1, need_weights=True)
        # k (batch_size, sequence_length, embedding_dimension)
        # v (batch_size, sequence_length, embedding_dimension)
        # attn_weight (batch_size, num_heads, sequence_length, sequence_length)

        x1  = torch.matmul(attn_weights, v)
        # Apply the attention weights to the values of the key. The shape of the result is (batch_size, sequence_length, embedding_dimension), and the sum across heads can be viewed as the output from this model.
        x1 += x2

        return x1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(5, 3, 64, 64)
mask1 = torch.ones((5, 3), dtype=torch.bool) # The shape of mask1 is (batch_size, sequence_length). All elements are True since there is no need to add masks for padding indices.
x2 = torch.randn(5, 8, 64, 64)
mask2 = torch.ones((5, 6), dtype=torch.bool) # The shape of mask2 is (batch_size, num_heads, sequence_length, sequence_length). All elements are True since there is no need to add masks for padding indices.
