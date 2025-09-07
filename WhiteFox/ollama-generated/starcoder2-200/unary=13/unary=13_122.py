
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(1024, 512)
        self.sigmoid = torch.nn.Sigmoid()

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = self.sigmoid(v1) # The sigmoid function is applied to the output of the linear transformation
        v3  = v1 * v2 # The output of the sigmoid function is multiplied by the output of the linear transformation, resulting in the gating mechanism.
        return v3

# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(512)
