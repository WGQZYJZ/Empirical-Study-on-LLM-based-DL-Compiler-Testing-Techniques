
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(d_model=64, num_heads=8)
 
    def forward(self, q, k, v):
        output = self.attn(q, k, v)[0] # Use the second return value of the multihead attention function to get the last layer output
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 64)
x2 = torch.randn(2, 64, 64)
