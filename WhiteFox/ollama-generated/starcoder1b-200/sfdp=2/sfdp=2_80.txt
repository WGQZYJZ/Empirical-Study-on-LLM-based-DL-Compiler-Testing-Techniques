
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = torch.nn.Linear(768, 10)
 
    def forward(self, x1, x2):
        hidden  = self.layer(x1)
        output   = hidden * 3 + x2
        return output


# Initializing the model
m = Model()


