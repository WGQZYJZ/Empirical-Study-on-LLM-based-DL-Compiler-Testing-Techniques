
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, input1):
        v1  = torch.mm(input1[0], input1[2])
        return torch.cat([v1] * len(input1), dim=3)


# Initializing the model