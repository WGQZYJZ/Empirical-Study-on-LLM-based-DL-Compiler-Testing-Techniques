
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 256)
 
    def forward(self, x1, x2, attn_mask):
        qk = query @ key.transpose(-2, -1) / math.sqrt(query.size(-1)) # Compute the dot product of the query and key, and scale it
        qk = qk + attn_mask # Add the attention mask to the scaled dot product
        attn_weight = torch.softmax(qk, dim=-1) # Apply softmax to the result
        output = attn_weight @ value # Compute the dot product of the attention weights and the value
        output = self.linear(output)
        return output

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64, 128, 320)
x2 = torch.randn(1, 128, 320, 640)
attn_mask = torch.randn(1, 64, 320, 640)
