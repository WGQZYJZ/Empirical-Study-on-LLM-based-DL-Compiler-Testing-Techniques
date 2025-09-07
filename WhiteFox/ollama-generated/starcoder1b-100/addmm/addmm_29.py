
class Model(torch.nn.Module):
    def __init__(self, inp):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(4, 16, 1, stride=2, padding=0)
        self.fc = torch.nn.Linear(8 * 8, 2)
        self.inp = inp
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1  # 1
        v3 = self.conv2(v2)  # 4
        v4 = torch.mm(v3, self.inp)  # input2 * inp
        v5 = v4 + self.inp  # (input2*inp) + inp
        return self.fc(v5)


# Initializing the model
m = Model()


