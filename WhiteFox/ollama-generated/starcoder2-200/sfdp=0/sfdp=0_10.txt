
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2, inv_scale=4305.798):  # This line shows the model definition
        scaled_dot_product = torch.matmul(x1, x2) / (inv_scale)
        attention_weights = scaled_dot_product.softmax(-1)
        output = attention_weights.matmul(torch.randn(50, 3))
        return output


# Initializing the model