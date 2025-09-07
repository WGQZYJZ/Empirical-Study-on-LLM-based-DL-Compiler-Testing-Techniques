
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(70, 2)
 
    def forward(self, x1, x2):
        scale  = torch.rsqrt(torch.tensor([70], dtype=x1.dtype, device=x1.device))
        query  = self.linear(x1)
        key    = self.linear(x2)
        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output              = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()
x1  = torch.randn(1, 30, 70)
x2  = torch.randn(1, 70, 2)
