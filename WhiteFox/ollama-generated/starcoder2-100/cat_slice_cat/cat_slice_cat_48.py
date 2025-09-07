
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0):
        t1 = torch.cat([x0, x0], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        t3 = t2[:, 0:size]
        t4 = torch.cat([t1, t3], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x0  = torch.randn(6, 500)
