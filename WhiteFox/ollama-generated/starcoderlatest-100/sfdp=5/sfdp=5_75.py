
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(3, 16)
 
    def forward(self, query, key, attn_mask):
        qk = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(query.size(-1)) + attn_mask
        qk = torch.softmax(qk, dim=-1)  # Apply softmax to the dot product of query and key
        output = torch.matmul(qk, key) # Compute the dot product of attention weights with key values
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 32, 64, 64)
key = torch.randn(8, 32, 64, 64)
attn_mask = (torch.rand(1, 1, query.size(-2), key.size(-3)) > 0).float() * -1e9
