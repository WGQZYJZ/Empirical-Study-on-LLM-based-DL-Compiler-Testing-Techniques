
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.query = torch.nn.Linear(64, 64) # Query layer
        self.key   = torch.nn.Linear(64, 64) # Key layer
        self.value = torch.nn.Linear(64, 64) # Value layer
    
    def forward(self, x):
        query = self.query(x)
        key   = self.key(x)
        value = self.value(x)

        attn_weight = (query @ key.transpose(-2, -1)) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        attn_weight = attn_weight + torch.eye(attn_weight.size(-1)).unsqueeze(0).to(attn_weight) * (-2**32+1)  # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(attn_weight, dim=-1)  # Apply softmax to the result

        output = (attn_weight @ value)  # Compute the dot product of the attention weights and the value

        return output


# Initializing the model
a = Attention()

# Inputs to the model
x2 = torch.randn(8, 64, 64)
