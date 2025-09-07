
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(8, 32)

    def forward(self, x1, x2):
        v1 = self.attn(x1, x2)[0] # Compute the output of the attention mechanism 
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64) # The shape is [B=4, T=8, D_k=8, H=1]
x2 = torch.randn(3, 4, 64, 64) # The shape is [B=3, T=5, D_v=32, H=1]
