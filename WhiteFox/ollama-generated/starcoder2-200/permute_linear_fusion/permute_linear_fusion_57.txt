
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.randn(20) # This line is important
        v2  = torch.permute(v1, dims=[-3], output_size=[-1])
        v3  = torch.nn.functional.linear(v2, self.weight, bias=None)
        return v3


# Initializing the model
m = Model()

