
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 8, kernel_size=1)

    def forward(self, query, key, value):
        v1 = self.conv(query).softmax(dim=-1).matmul(value) # v1 is computed in the first line of code above
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
q1  = torch.randn(1, 8, 64, 64)
k1  = torch.randn(1, 8, 64, 64)
v1  = torch.randn(1, 8, 64, 64)
