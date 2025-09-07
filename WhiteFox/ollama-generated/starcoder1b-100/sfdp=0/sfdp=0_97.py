
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.DotTable()
 
    def forward(self, x1, x2):
        scale = math.sqrt(x2.size(-2))
        scaled_dot_product = self.scaled_dot_product((x1 * x2).contiguous().view(x1.shape[0], -1), scale)
        weights = scaled_dot_product.softmax(-1)
        output = weights.matmul(x2)
        return output


# Inputs to the model
x1  = torch.randn(3, 64, 64)
x2  = torch.randn(64, 64)
