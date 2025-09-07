
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.MultiheadAttention(8, 2)
 
    def forward(self, x1, key, value):
        scaled_dot_product = torch.matmul(x1, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
key = torch.randn(2, 8, 64, 64)
value = torch.randn(3, 8, 64, 64)
