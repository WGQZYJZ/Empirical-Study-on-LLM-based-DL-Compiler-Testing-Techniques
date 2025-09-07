
class Model(torch.nn.Module):
    def __init__(self, heads=8):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(3, 16)
        self.projector = torch.nn.Linear(16 * heads, 2048)
        self.fc = torch.nn.Linear(2048, num_classes)
 
    def forward(self, x1):
        v1, _ = self.attention(x1, x1, x1) # multi-head attention: input (queries, keys, values) output (outputs, key_attn_weights, query_attn_weights)
        v2  = torch.mean(v1, dim=-2) # Take the mean over time
        v3  = self.projector(v2) # Apply a linear projection
        v4  = torch.relu(v3) # Perform relu operation on the projected tensor
        v5  = self.fc(v4)  # Apply final classification layer
        return v5


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(20, 3, 64, 64)
