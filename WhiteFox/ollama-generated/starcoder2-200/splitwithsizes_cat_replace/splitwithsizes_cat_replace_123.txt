
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.split(x1, 32768, 0) + torch.split(x1, 57344, 0), torch.split(x1, 81920, 0), torch.cat([torch.split(x1, 32768, 0)[i] for i in range(len(torch.split(x1, 32768, 0)))], dim=1)


# Initializing the model and inputs to it
m = Model()
x1 = torch.randn((54976 + 1), 4, 32768, 16)
