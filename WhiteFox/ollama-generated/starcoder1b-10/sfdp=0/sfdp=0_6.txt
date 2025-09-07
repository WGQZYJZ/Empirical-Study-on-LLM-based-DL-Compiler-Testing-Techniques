
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        scaled_dot_product = torch.matmul(v1, x1.transpose(-2, -1)) / torch.sqrt(torch.square(x1).sum(dim=-1, keepdim=True)).clamp_min(min=eps)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(v1)
        return output


# Initializing the model
m = Model()


