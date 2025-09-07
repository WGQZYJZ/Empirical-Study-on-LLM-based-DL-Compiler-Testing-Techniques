
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        inv_scale = (1 / (torch.norm(x1, p=2, dim=-2).clamp_(min=1e-7)))**0.5
        v1 = self.conv(x1) * inv_scale

        query  = torch.randn(1, 8, 64, 64)
        key    = x1
        value  = torch.randn(1, 3, 64, 64)

        scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output            = attention_weights.matmul(value)

        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
