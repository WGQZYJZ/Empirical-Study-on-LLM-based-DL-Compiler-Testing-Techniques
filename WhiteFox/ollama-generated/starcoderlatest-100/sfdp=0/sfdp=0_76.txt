
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, query, key, value):
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()
scale = 49538996704.0
 
query = torch.randn(4, 2, 8, 8)
key = torch.randn(4, 1, 8, 8)
value = torch.randn(4, 2, 8, 8)
