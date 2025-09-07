
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        x1 = self.attention(q1, k1, v1)
        return x1


# Initializing the model
m = Model()

 # Inputs to the model
q1 = torch.randn(32, 8, 56, 56)
k1 = torch.randn(8, 8, 28, 28)
v1 = torch.randn(8, 8, 28, 28)
