
class Model(torch.nn.Module):
    def __init__(self, k=20):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.conv2d(x1, self.conv) 
        v2 = torch.nn.functional.batch_norm(v1)


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10, m.k, 384, 672)
__output__  = m(x1)

