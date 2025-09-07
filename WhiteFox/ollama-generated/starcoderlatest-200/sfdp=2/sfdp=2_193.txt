
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(10, 2, dropout=0.1)
 
    def forward(self, q1, k1, v1):
        output, attn = self.attention(q1, k1, v1)
        return output


# Initializing the model
m = Model()
# Inputs to the model
x1 = torch.randn(1, 5, 64, 64)
k1 = x1 # Same input for both keys and values
v1 = k1
