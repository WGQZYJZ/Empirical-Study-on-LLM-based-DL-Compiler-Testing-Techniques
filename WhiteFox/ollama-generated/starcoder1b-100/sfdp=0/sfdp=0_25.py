
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        inv_scale = 1.0 / (v1 ** 2).sum(-1, keepdim=True).sqrt()
        query = v1
        key   = x1
        value = x1 * 0.5
        attention_weights = scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        output = attention_weights.matmul(value)
        return output


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
