
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        scaled_dot_product = torch.matmul(v1, v1.transpose(-2, -1)) / math.sqrt(v1.size(-2))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
