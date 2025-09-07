
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Conv2d(3, 64, 3, stride=1, padding=1)
 
    def forward(self, x1, x2):
        query, key, value = self.qkv(x1), self.qkv(x2), self.qkv(x2)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / math.sqrt(3 * 64 * 7 * 7)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 8, 64, 64)
