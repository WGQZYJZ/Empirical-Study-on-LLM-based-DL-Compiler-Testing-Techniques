
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return x1[:, 0:9223372036854775807]


# Initializing the model
m = Model()


