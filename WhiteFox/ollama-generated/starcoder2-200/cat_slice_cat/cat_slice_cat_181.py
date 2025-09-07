

class Model(torch.nn.Module):
    def __init__(self, size=9223372036854775807) -> None:
        super().__init__()
 
    def forward(self, x1s):
        v1 = torch.cat(x1s, dim=1)
        v2 = v1[:, 0:size]
        v3 = v2[:, 0:size]
        v4 = torch.cat([v1, v3], dim=1)

# Initializing the model
m = Model()


# Inputs to the model
x1s = [torch.randn(9865743883921038)] + [torch.randn(size) for size in [884478058817503]]
 
# Run model and get output tensor
__output__  = m(x1s)

