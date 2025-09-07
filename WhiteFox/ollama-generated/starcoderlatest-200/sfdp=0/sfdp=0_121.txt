
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 4, bias=False)
 
    def forward(self, x1, x2):
        qkv  = self.qkv(x1).chunk(4, dim=-1)
        query = qkv[0]
        key = qkv[1]
        value = qkv[2]
 
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / 16.0
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(value)
        return output


# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
x2 = torch.randn(2, 3, 64, 64)
