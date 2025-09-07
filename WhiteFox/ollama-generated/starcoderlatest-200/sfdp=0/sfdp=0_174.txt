
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.attention = torch.nn.Linear(768, 256)
 
    def forward(self, x1, x2):
        scaled_dot_product = torch.matmul(x1, x2.transpose(-2, -1)) / math.sqrt(x1.size(-1))
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x2)
        return output


# Initializing the model
m = Model()

# Inputs to the model
query = torch.randn(3, 768, 64, 64)
key = torch.randn(256, 768, 12, 12)
value = torch.randn(3, 256, 12, 12)
