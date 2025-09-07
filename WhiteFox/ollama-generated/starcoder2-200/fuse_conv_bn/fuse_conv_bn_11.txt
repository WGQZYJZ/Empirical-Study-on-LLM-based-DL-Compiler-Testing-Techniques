
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.conv1d(x1, self.linear.weight)
        v2  = torch.nn.functional.batch_norm(v1, self.linear.bias)

        return v2
# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(4, 320, 596)
