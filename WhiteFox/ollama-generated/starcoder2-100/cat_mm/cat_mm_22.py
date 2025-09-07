
class Model(torch.nn.Module):
    def __init__(self, n_input1, n_input2):
        super().__init__()
        self.mm = torch.nn.functional.linear

    def forward(self, x1, x2): 
        v1  = self.mm(x1, x2)
        v2  = torch.cat([v1] * len(self.x1), dim=0)
        return v2


# Initializing the model