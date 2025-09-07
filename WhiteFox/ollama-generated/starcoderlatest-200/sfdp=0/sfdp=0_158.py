
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, q1, k1, v1):
        x  = torch.matmul(q1, k1.transpose(-2, -1))
        attention_weights  = x / math.sqrt(k1.shape[-1])
        output = self.attention(v1, attention_weights)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64, 64)
y1 = torch.randn(1, 64, 64)
z1 = torch.randn(1, 64, 64)
