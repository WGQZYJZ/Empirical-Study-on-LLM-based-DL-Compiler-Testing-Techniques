
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 12)
 
    def forward(self, q, k, v):
        attention_weights = self.attention(q, k, v)
        output = attention_weights[0] * v
        return output


# Initializing the model
m = Model()


# Inputs to the model
q = torch.randn(128, 64, 56, 56).permute(1, 0, 2, 3)
k = torch.randn(32, 64, 28, 28).permute(1, 0, 2, 3)
v = torch.randn(32, 64, 28, 28).permute(1, 0, 2, 3)


