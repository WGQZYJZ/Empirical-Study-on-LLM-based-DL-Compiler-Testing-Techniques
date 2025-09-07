
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        # scaled_dot_product = torch.matmul(query, key.transpose(-2, -1)) / inv_scale
        query = self.conv(x1)
        output = torch.matmul(query, self.conv.weight).softmax(dim=-1) * self.conv.weight
        return output


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
