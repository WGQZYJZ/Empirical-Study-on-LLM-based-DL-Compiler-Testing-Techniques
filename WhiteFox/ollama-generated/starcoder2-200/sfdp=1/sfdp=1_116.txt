
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(8, 2)
    
    def forward(self, x1):
        v1, _  = self.att(query=x1, key=x1, value=x1)
        return v1

# Initializing the model
m  = Model()

# Input to the model
x1  = torch.randn(8, 8)
