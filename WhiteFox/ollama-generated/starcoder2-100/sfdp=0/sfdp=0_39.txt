
class Model(torch.nn.Module):
    def __init__(self, inv_scale):
        super().__init__()
        self.inv_scale = inv_scale

    def forward(self, q1, k1, v1):
        scaled_dot_product  = torch.matmul(q1, k1.transpose(-2, -1)) / self.inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(v1)

        return output


# Initializing the model
m  = Model(0.7)

# Inputs to the model
q1  = torch.randn(32, 48, 512)
k1  = torch.randn(32, 48, 512)
v1  = torch.randn(32, 48, 512)

 