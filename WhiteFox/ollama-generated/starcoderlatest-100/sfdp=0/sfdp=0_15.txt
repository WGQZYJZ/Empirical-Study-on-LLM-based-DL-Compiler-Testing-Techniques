
class Attention(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inv_scale):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return output

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = Attention()
 
    def forward(self, x1, x2, inv_scale):
        x3 = self.attention(x1, x2, inv_scale)
        return x3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(64, 512)
x2 = torch.randn(64, 512)
inv_scale = 0.01
