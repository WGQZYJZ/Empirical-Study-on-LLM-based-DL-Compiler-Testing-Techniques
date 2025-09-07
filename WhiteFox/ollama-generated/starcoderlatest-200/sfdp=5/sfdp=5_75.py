
class Model(torch.nn.Module):
    def __init__(self, num_attention_heads=16):
        super().__init__()
        self.attn_mask = torch.ones([1, 32, 32], dtype=torch.float32)
 
    def forward(self, query, key, value):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + self.attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(1, 32, 32)
key = torch.randn(1, 64, 32)
value = torch.randn(1, 64, 32)
