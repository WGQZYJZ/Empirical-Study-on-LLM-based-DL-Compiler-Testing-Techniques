
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, qk):
        scaled_dot_product = torch.matmul(qk[0], qk[1].transpose(-2,-1)) / 32
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(qk[2])

        return output


# Inputs to the model
x1 = torch.randn(8, 160, 56, 56)
x2 = torch.randn(320, 160, 8, 8)
