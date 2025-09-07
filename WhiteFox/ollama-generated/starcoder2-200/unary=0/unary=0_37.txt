

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1): 
        v1 = self.conv0(x1)
        v2 = self.conv0(v1)
        v3 = torch.mean(v2, 1, keepdim=True).clamp(min=-5., max=5.)
        v4 = self.conv0(self.conv1(torch.nn.functional.relu(x1 + v3)))
        return torch.nn.functional.relu(torch.cat((
            x1 / (2 ** 8), 
            self.conv0(v1) * .5, 
            self.conv0(torch.sqrt(self.conv0(self.conv0(v4)))) * .7978845608028654
        ), 1))

m = Model()
x1 = torch.zeros((32, 3, 56, 56))
