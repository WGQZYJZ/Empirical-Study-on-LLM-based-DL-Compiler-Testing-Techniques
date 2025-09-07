
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, t1):
        v1 = torch.cat((t1[:, 0:9223372036854775807], t1[:, size:]), dim=1)
        return v1


# Initializing the model
m = Model()


# Inputs to the model
t1 = torch.randn(2, 10, 256, 256)
