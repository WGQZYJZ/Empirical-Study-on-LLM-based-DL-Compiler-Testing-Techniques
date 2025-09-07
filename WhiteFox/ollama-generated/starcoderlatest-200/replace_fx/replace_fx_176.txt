
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.dropout(x1, p=0.25)
        v2 = torch.rand_like(x1, dtype=torch.float32)
        return torch.cat((v1, v2), dim=2)


# Initializing the model
m = Model()
gm = pytorch_graph(_input=x1)

