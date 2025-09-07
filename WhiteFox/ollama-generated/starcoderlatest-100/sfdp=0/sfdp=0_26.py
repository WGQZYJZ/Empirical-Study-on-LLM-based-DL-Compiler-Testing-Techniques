
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = torch.nn.Linear(512, 64)
 
    def forward(self, x1):
        v1 = self.fc(x1) * math.sqrt(0.75)
        v2 = torch.matmul(v1, v1.transpose(-1,-2)) / (math.pi * math.pow(inv_scale, 4/3))
        v3 = F.softmax(v2, dim=0).detach().clone()
        v4 = torch.matmul(v3, self.fc(x1).view(512, -1)).transpose(-1,-2)
        output = (x1 + v4) * math.pow(inv_scale, 1/3)
        return output


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
