
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.qkv = torch.nn.Linear(3, 8, bias=True)
 
    def forward(self, x1):
        v1, k1, v2, k2 = self.qkv(x1).chunk(4, dim=-1)
        scaled_dot_product = torch.matmul(v1, k2.transpose(-2, -1)) / np.sqrt(k1.shape[-1])
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v2)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
