
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 12, bias=False)
 
    def forward(self, x1):
        q1, k1, v1 = self.qkv(x1).chunk(3, dim=-1)
        q1 = q1.transpose(-2, -1)
        scaled_dot_product = torch.matmul(q1, k1.transpose(-2, -1)) / math.sqrt(v1.shape[-1])
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)
        return output


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
