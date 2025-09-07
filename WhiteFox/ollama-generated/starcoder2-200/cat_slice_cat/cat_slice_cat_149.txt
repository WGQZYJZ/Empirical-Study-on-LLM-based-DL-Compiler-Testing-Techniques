
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x2):
        v1 = torch.cat([x2[0], x2[-1]], dim=1)
        return v1[:, 0:9223372036854775807]


# Initializing the model and running it for inputs.
m_ = Model()
