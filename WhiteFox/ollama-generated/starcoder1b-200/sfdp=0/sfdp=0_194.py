
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x):
        x_scaled_dot_product = torch.matmul(x, x.transpose(-2, -1)) / math.sqrt(float(x.shape[0]))
        x_attention_weights = F.softmax(x_scaled_dot_product, dim=-1)
        output = torch.matmul(x_attention_weights, self.conv(x).view((x.shape[0], -1)))
        return output


# Initializing the model
m = Model()
x  = torch.randn(4, 3, 64, 64)
