
class Model(torch.nn.Module):
    def __init__(self, hidden_size=512):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, hidden_size)
 
    def forward(self, qk, kq):
        v1  = qk
        v2  = kq
        output  = self.attention(v1, v2)[0]
        return output
 
 # Initializing the model
m = Model()

 # Inputs to the model
qk  = torch.randn(4, 8, 64, 64)
kq  = torch.randn(4, 8, 64, 64)
