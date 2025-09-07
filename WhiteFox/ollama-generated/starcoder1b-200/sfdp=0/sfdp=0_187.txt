
class Model(torch.nn.Module):
    def __init__(self, scale=10000):
        super().__init__()
        self.scale = scale
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / float(self.scale)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m  = Model()


# Inputs to the model
x1, x2 = torch.randn(2, 3, 64, 64), torch.randn(2, 8, 64, 64)
