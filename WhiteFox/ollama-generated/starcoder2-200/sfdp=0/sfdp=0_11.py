
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):

        v3 = torch.matmul(x1, x2) / 0.7071067811865476
        v5  = scaled_dot_product.softmax(-2, dim=-1)
        v9  = v3 + 1
        v10 = v3 * v9 
        return v10


# Initializing the model
m  = Model()

# Inputs to the model
__input__  = torch.randn(48, 512), torch.randn(48, 512)
