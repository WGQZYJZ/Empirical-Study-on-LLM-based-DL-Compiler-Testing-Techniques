
class Model2(torch.nn.Module):
    def __init__(self, other1=0., other2=None, name='Model2'):
        super().__init__()
 
        self._other = torch.tensor([[[[other1]]], device="cuda")
        
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x):
        v1 = self.conv(x)

        if other2 is not None:
            v4  = v1 - other2
            return v4
        else:
            v5  = v1 - self._other
            return v5


# Initializing the model