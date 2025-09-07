
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(...)

    def forward(self, x1):
        t1 = x1  # Linear transform on input tensor (i.e., permute on the output tensor of the linear function).
        t2 = self.linear(t1)
        return t2


# Inputs to the model
x1  = torch.randn(...)  # Inputs to the model
