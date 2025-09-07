
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, x1, x2):
        qk = self.attention(x1, x2) # Apply the attention mechanism
        return qk


# Initializing the model
m = Model()
q1 = torch.randn(4, 3, 64, 64)
k2 = torch.randn(4, 8, 64, 64)
