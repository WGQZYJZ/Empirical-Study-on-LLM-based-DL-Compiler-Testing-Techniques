
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention()
 
    def forward(self, query, key, value):
        attention_weights = self.attention(query, key, value)[0]
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
q1 = torch.randn(32, 8, 64, 64)
k1 = torch.randn(8, 16, 64, 64)
v1 = torch.randn(16, 8, 64, 64)
