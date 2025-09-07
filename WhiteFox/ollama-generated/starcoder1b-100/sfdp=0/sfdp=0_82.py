
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        scaled_dot_product = torch.matmul(x1, x1.transpose(-2, -1)) / math.sqrt(64 * 64)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
