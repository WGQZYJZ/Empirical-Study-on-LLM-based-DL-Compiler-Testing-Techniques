
class Model(torch.nn.Module):
    def __init__(self, d_k = int()):
        super().__init__()
        self.linear  = torch.nn.Linear()
        self.attn  = torch.nn.MultiheadAttention(d_model = d_k)

    def forward(self, query, key):
        v1  = self.linear(key)
        v2  = v1 + attn_mask  # Add the attention mask to the result of applying the linear layer to the value tensor
        v3  = torch.softmax(v2, dim = ) # Apply softmax to the output of applying the linear layer to the value tensor
        v4  = v3 @ query  # Compute the dot product of the dropout output and the query tensor
        return v4

# Initializing the model with `d_k = 8`
m  = Model(d_k = 8)

# Inputs to the model: key, value tensors.
key  = torch.randn(32, 10, 64)
query  = torch.randn(32, 9, 64).
value  = torch.randn(32, 7, 64)
attn_mask = torch.full((8, 9), -1e9) # Generate an attention mask of size (8, 9) that's filled with very large negative numbers

