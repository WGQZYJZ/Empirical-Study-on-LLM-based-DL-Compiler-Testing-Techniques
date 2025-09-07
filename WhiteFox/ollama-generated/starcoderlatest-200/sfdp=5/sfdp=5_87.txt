
class AttentionModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value):
        attn_mask = torch.arange((query.size(0) + key.size(0))) > (torch.arange((query.size(0))) * key.size(0))
        qk  = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk  = qk + attn_mask  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the dropout output and the value
        return output


# Initializing the model
m = AttentionModel()

# Inputs to the model
query = torch.randn(4, 3, 64, 64)
key   = torch.randn(8, 3, 64, 64)
value = torch.randn(10, 3, 64, 64)
