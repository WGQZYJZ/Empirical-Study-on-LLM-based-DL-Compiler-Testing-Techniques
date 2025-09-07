
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 32)
 
    def forward(self, query, key, attn_mask=None):
        qk = self.attn(query, key, attn_mask)[0] # Compute the scaled dot-product attention
        return qk


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(16, 8, 64, 64)
key = torch.randn(16, 8, 256, 256)
attn_mask = torch.randint(low=0, high=2, size=(16, 1, 64, 64))  # Set the attention mask to all zeros except one on the last position in each query tensor. The shape of attn_mask is (batch_size, num_heads, seq_len, seq_len)
