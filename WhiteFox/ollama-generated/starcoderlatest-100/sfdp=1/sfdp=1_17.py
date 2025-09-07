
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        a  = self.attention(q1, k1, v1)
        return a

 # Initializing the model
m = Model()

 # Inputs to the model
query   = torch.randn(2, 8, 32, 16)
key     = torch.randn(2, 8, 32, 16)
value    = torch.randn(2, 8, 32, 16)
