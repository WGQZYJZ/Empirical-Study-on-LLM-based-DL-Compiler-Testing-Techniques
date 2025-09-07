
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 128)
 
    def forward(self, query, key, value):
        # query: (batch_size, num_heads, qkv_len, embed_dim),
        #   where num_heads is the number of heads and embed_dim is the embedding dimension.
        #   It can be obtained by `torch.split(..., ..., dim=2)` where `-1` means split along last dimension.
        # key: (batch_size, num_heads, kv_len, embed_dim) 
        # value: (batch_size, num_heads, kv_len, embed_dim)
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key
        qk = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value 
        return output

# Initializing the model
m = Model()

 # Inputs to the model
query = torch.randn(4, 8, 20, 19)
key = torch.randn(3, 5, 67, 19)
value = torch.randn(4, 7, 42, 19)
