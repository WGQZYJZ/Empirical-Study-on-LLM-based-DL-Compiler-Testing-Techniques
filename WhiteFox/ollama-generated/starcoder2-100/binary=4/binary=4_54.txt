
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(512, 5)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other_tensor # Add another tensor to the output of linear transformation

# Initializing the model
m = Model()
other_tensor = torch.randn(34560)
__output__  = m(input)

