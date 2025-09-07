
class Model(torch.nn.Module):
    def __init__(self, d_model=32):
        super().__init__()
        self.d_model = d_model

    def forward(self, q, k, v):
        inv_scale = math.sqrt(1 / (self.d_model))
        scaled_dot_product  = torch.matmul(q, k.transpose(-2, -1)) / inv_scale
        attention_weights   = scaled_dot_product.softmax(dim=-1)
        output              = attention_weights.matmul(v)
        return output


# Initializing the model
m = Model()

# Inputs to the model
q  = torch.randn(8, 32, 64, 64)
k  = torch.randn(8, 32, 64, 64)
v  = torch.randn(8, 32, 64, 64)
