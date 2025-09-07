
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        v1 = torch.nn.functional.convXd(...)
        v2 = torch.nn.functional.batch_norm(...)
        output = v1 + v2
        return output


# Inputs to the model
x  = torch.randn(1, 2, 2)
