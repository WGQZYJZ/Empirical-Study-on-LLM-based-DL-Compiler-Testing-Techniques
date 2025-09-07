
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, input1):  # Input is a random tensor
        v1 = torch.nn.functional.dropout(input1)

        v2 = torch.nn.functional.linear(v1, torch.rand_like(input1))

        return v2


# Initializing the model
m  = Model()
__output__  = m(torch.randn(30))
