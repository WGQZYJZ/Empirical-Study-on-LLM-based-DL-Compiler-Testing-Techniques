
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(embed_dim, num_heads)
 
    def forward(self, x1, x2):  # input tensor 1 and the input tensor 2 may have different shapes in this case!
        vq  = self.attn(query=x1, key=x2, value=x2)[0] + v2
        return vq


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(16, 48) # this is a query vector
x2  = torch.randn(32, 48) # this is the key-value matrix in attention mechanism

