
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        scaled_dot_product = torch.matmul(v2, x1.transpose(-2, -1)) / math.sqrt(x1.shape[0] * x1.shape[1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x1)
        return output


# Initializing the model
m = Model()

