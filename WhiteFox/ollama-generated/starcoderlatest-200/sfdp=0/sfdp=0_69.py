
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 12)
 
    def forward(self, x1, key, value):
        attention_weights = self.attention(x1, key, value)
        scaled_dot_product = attention_weights[0]
        output = attention_weights[0].matmul(value)
        return output

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
key = torch.randn(12, 8, 64, 64)
value = torch.randn(12, 8, 64, 64)
