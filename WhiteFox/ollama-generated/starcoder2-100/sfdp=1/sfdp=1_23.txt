
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attn = torch.nn.MultiheadAttention(256, 8)
 
    def forward(self, x1):
        v1, _ = self.attn(x1[:, None], x1[:, None]) # Compute the dot product of the query and key tensors, then softmax is applied to the scaled dot product to get a dropout output, and finally compute the dot product of the dropout output and value tensor
        return v1

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(32, 64)
__output__  = m(x1)


