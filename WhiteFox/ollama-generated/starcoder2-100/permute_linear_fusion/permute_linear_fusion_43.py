
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.randn(3072) # Initializing the first input.
        t1  = x1.permute([0, 2, 1])
        v2  = torch.nn.functional.linear(t1, self.weight)
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.rand(3072, 64).transpose([0, 1]) # Initialize an input tensor with shape (64, 3072) in pytorch, permute it to make it with shape (3072, 64) and transpose it to the form of (64, 3072), this will be used as main input for the first operation.


__output__  = m(x1)
