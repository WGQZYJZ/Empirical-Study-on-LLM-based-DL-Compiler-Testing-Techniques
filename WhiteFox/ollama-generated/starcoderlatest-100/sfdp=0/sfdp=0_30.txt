
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = ScaledDotProductAttention()
 
    def forward(self, query, key, value, scale_factor):
        v1 = scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(32, 8, 64, 64)
x2 = torch.randn(32, 8, 64, 64)
x3 = torch.randn(32, 8, 64, 64)
scale_factor = float32([0.5])

 # Executing the model on given inputs
output = m(query=x1, key=x2, value=x3, scale_factor=scale_factor)

 