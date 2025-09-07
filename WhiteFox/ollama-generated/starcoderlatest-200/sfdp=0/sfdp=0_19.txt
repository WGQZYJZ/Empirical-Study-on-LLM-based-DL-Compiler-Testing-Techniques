
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.ScaledDotProductAttention()
 
    def forward(self, query, key, value, scale):
        scaled_dot_product = self.scaled_dot_product(query, key, value, scale)
        attention_weights = scaled_dot_product[0]
        output = scaled_dot_product[1]
        return output

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 512, 512)
x2 = torch.randn(2, 8, 512, 512)
