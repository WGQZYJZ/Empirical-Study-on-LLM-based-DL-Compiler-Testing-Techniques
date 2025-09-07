
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3,8, bias=False)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = v1 - other # 'other' is a parameter to be generated randomly 
        v4 = torch.relu(v2)
        return v4

m  = Model()

