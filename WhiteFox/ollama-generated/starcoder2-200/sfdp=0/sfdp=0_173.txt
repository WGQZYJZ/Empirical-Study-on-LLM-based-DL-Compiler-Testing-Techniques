

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scale  = torch.Tensor([10])
        self.q  = torch.randn(4, 32)
        self.k  = torch.randn(4, 32)
        self.v  = torch.randn(4, 64, 8)

    def forward(self):
        scaled_dot_product  = torch.matmul(self.q, self.k.transpose(-1,-2)) / self.scale[-1]
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(self.v)
        return output


