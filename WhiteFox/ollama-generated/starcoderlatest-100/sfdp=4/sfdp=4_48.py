
class Attention_model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention()
 
    def forward(self, x1, key, query, value, attn_mask):
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Attention_model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
key = torch.randn(8, 16, 128, 128)
query = torch.randn(32, 16, 56, 56)
value = torch.randn(32, 16, 100, 100)
attn_mask = torch.randn(16, 64, 20, 8)
