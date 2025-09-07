
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.Linear(768, 12)
 
    def forward(self, qk, attn_mask, value):
        v1 = qk @ key.transpose(-2, -1) / math.sqrt(key.size(-1)) # Compute the dot product of the query and key, and scale it
        v2 = v1 + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(v2, dim=-1)  # Apply softmax to the result
        output = attn_weight @ value  # Compute the dot product of the attention weights and the value
        return output


# Initializing the model
m = Model()

# Inputs to the model
qk  = torch.randn(8, 12, 64, 64)
attn_mask = torch.rand(1, 1, 64, 64)
value = torch.randn(32, 768, 32, 32)
