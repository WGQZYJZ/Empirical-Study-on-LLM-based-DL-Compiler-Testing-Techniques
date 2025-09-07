
class Transformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, x2):
        v1 = self.conv(x1) * 0.5
        v2 = self.conv(x2) * 0.7071067811865476
        scaled_dot_product = torch.matmul(v1, v2.transpose(-2, -1)) / np.sqrt(32)
        attention_weights = scaled_dot_product.softmax(dim=-1)  # softmax
        output = attention_weights.matmul(v2)
        return output


# Initializing the model
m = Transformer()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
