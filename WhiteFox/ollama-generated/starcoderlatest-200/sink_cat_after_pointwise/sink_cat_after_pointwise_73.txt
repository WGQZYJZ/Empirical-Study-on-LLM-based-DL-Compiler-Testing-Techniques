
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        # Please add your own logic here to generate the model example
        v = torch.cat([x1[:,:,:1], x1[:,:,1:]], dim=1)
        t3 = torch.relu(v)
        return t3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(2, 4, 8)
