
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1)
        v2  = conv(v1)

        v3  = torch.nn.functional.batch_norm(v2)
        return v3

# Initializing the model
m  = Model()

