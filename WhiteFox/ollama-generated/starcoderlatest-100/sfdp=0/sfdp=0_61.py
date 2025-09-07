
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.att = torch.nn.MultiheadAttention(3, 8)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(float(3))
        attention_weights = self.att(scaled_dot_product, scaled_dot_product)[0]
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 64, 72, 72)
x2 = torch.randn(8, 64, 64, 64)
