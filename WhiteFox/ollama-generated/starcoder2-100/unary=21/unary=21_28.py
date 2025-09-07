
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,__input__):
        v0 = self.conv(__input__)
        v1  = torch.tanh(v0)
        return v1


# Initializing the model
m = Model()

