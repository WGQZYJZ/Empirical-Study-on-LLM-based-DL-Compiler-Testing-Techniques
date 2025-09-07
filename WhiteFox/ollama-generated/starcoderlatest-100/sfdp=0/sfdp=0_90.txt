
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.matmul = torch.nn.Linear(1024, 64)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / 3.14 * (sqrt(key_dim) * key_scale)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()
x1 = torch.randn(2, 64, 300, 768)
x2 = torch.randn(2, 64, 300, 768)
