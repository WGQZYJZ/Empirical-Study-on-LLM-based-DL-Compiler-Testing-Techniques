
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention(16, 8)
 
    def forward(self, q1, k1, v1):
        attn_weight, _ = self.attn_layer(q1, k1, v1) # Compute scaled dot-product attention weights
        output = attn_weight @ v1 # Compute weighted sum of the value tensor
        return output


# Initializing the model
m = Model()

# Inputs to the model
q1 = torch.randn(8, 32, 64)
k1 = torch.randn(8, 32, 64)
v1 = torch.randn(8, 32, 64)
