
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, query, key, value, scale):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
query = x1
key = query
value = key
scale = torch.sqrt(torch.tensor([1]))
