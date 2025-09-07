
class Model(torch.nn.Module):
    def __init__(self, k):
        super().__init__()

    def forward(self, x1, y1):
        t2 = torch.cat([x1, y1], dim=0) # concat along batch dimension (dim 0)
        t3 = t2.view(-1, self.k ** 2 + 4)

        return t3


# Initializing the model
m = Model(5)

# Inputs to the model
x1 = torch.randn(8, 9) # Input tensor 1 (containing 7 dimensions) with 8 data points and 9 features per data point
y1 = torch.randn(4320,) # Input tensor 2 of shape [4320]
__output__  = m(x1, y1)

