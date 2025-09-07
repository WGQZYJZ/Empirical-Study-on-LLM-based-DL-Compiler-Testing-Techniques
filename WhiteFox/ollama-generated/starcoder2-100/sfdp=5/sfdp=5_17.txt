
class Model(torch.nn.Module):
    def __init__(self, ):
        super().__init__()
        self.self_attn  = torch.nn.MultiheadAttention(1024, 6)
 
    def forward(self, x1):
        x3, attn = self.self_attn(x1, x1)
        return x3, attn


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(640, 20579)
__output__, __attn__   = m(x1)

