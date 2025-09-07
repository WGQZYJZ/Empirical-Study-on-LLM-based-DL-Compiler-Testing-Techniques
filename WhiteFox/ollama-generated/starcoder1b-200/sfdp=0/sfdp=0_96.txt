
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.linear = torch.nn.Linear(8, 1)
 
    def forward(self, x):
        v = self.conv(x)
        m = v.mean(-1, keepdim=True).expand_as(v)
        scaled_dot_product = torch.matmul(v, m) / (self.linear(m) + 1e-6)
        attention_weights = scaled_dot_product.softmax(dim=-1)
        output = attention_weights.matmul(x)
        return output


# Initializing the model
model = Model()

