
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, query, key, value):
        v1 = self.attn(query, key, value, attn_mask=key)[0]
        return v1


# Initializing the model
m = Model()

# Inputs to the model
q = torch.randn(256, 8, 4, 16) # q is a batch of query tokens with dimension (batch_size, num_heads, from_seq_length, to_seq_length)
k = torch.randn(256, 8, 4, 32) # k is a batch of key tokens with dimension (batch_size, num_heads, from_seq_length, to_seq_length)
v = torch.randn(256, 8, 4, 64) # v is a batch of value tokens with dimension (batch_size, num_heads, from_seq_length, to_seq_length)
