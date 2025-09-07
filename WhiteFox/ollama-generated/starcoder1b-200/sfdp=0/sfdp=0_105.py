
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        scaled_dot_product = torch.matmul(v1, v2).softmax(-1)
        attention_weights = scaled_dot_product.matmul(v2)
        output = attention_weights.matmul(v1)
        return output

# Initializing the model
m = Model()


