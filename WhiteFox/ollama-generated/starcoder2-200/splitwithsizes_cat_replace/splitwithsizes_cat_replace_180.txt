
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()

    def forward(self, x1):
        v1  = torch.split(x1, [8], 0) # [torch.Tensor, torch.Tensor]
        v2  = torch.cat([v1[i] for i in range(len(v1))], 0)
        return v2

# Initializing the model with default value of `dim`
m  = Model()


# Inputs to the model - default value of dim
x1   = torch.randn(3, 8) # [torch.Tensor]


