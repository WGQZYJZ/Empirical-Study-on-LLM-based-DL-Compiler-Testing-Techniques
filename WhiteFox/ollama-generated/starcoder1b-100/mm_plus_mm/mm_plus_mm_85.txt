
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.input1 = torch.nn.Linear(128, 32)
        self.input2 = torch.nn.Linear(32, 64)
        self.input3 = torch.nn.Linear(64, 96)
        self.input4 = torch.nn.Linear(96, 128)
        self.conv = torch.nn.Conv2d(1, 32, 3, stride=2, padding=0)
 
    def forward(self, x1, x2):
        v1  = self.input1(x1)
        v2  = self.input2(v1)
        v3  = self.input3(v2)
        v4  = self.input4(v3)
        v5  = torch.mm(v1, v2)
        v6  = v5 + v4
        return v6


# Initializing the model
m = Model()


