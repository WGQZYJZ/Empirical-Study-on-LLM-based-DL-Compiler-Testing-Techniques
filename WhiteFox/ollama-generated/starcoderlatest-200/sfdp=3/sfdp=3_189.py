
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layernorm_1 = torch.nn.LayerNorm([20, 30]) # Layer norm before QK
        self.attn = torch.nn.MultiheadAttention(8, 4) # Attention layer with head dim of 4
        self.dropout = torch.nn.Dropout(p=dropout_p)
 
    def forward(self, query, key):
        v1 = self.layernorm_1(query) # Apply layer norm to the query
        v2, v3 = self.attn(v1, v1, v1) # Compute attention using multihead attention with head dim of 4
        v4 = self.dropout(v2) # Dropout applied to the multihead attention output
        return v4


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 8, 30, 60) # Query tensor of shape (batch_size, num_heads, key_length, value_length)
key = torch.randn(1, 8, 20, 50) # Key tensor of shape (batch_size, num_heads, query_length, value_length)
