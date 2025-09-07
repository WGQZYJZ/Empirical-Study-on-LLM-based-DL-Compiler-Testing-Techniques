
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.ScaledDotProductAttention(temperature=1)
 
    def forward(self, query, key, value, scale):
        scaled_dot_product = self.scaled_dot_product(query, key, value, scale)
        attention_weights = scaled_dot_product[0]
        output = scaled_dot_product[1]
 
        return output, attention_weights


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 8, 56, 56)
scale = torch.tensor([0.97], dtype=torch.float32).unsqueeze(-1).repeat(1,1,4,1)
__output__, __attention_weights__ = m(x1, x1, x1, scale)

