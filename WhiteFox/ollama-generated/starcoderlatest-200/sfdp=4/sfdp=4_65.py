
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn_layer = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        out1 = self.attn_layer(q1, k1, v1)
        return out1[0]  # Only output the final projected layer


# Initializing the model
m = Model()
 
# Inputs to the model
q1 = torch.randn(4, 5, 64, 64)
k1 = torch.randn(8, 5, 32, 32)
v1 = torch.randn(8, 5, 32, 32)
