
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim=128, num_heads=4)
 
    def forward(self, q1, k1, v1):
        attn_weight  = torch.softmax(self.attn(q1, k1, v1), dim=-1) # Compute attention weights
        output = attn_weight @ v1  # Compute the dot product of the attention weights and the value
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64)
k1 = torch.randn(8, 128, 64)
v1 = torch.randn(8, 128, 64)
