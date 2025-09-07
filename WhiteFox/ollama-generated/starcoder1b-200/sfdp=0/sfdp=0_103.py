
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        x_mean   = x1.mean(-1).mean(-1)
        scaled_dot_product = torch.matmul(x_mean, x1)
        attention_weights  = scaled_dot_product.softmax(dim=-1)
        output            = attention_weights.matmul(x1)
        return output


# Inputs to the model
query    = torch.randn(4, 8, 5, 5)
key      = torch.randn(4, 8, 5, 5)
value    = torch.randn(4, 3, 5, 5)
