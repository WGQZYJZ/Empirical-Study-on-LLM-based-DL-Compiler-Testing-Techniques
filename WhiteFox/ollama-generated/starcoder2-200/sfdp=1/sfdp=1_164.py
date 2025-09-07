
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 4)
 
    def forward(self, x1): 
        v1, v2 = self.attention(query=x1, key=x1)
        return v1


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(32, 8, 64, 64) 
 __output__  = m(x1)
 
 