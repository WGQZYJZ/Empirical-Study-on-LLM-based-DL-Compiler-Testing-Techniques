
class Attention(torch.nn.Module):
    def __init__(self, nhead=1):
        super().__init__()

        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        scaled_dot_product  = torch.matmul(v1, v1.transpose(-2, -1)) / inv_scale
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output  = attention_weights.matmul(value)
        return output


# Initializing the model
m  = Attention()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)