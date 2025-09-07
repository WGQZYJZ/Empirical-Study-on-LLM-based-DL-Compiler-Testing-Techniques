
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1).pow(2)
        v2 = torch.zeros_like(v1)
        v3 = v1 * 0.5
        v4 = v3.mul_(v3)
        v5 = v1.pow(2)
        v6 = torch.empty((v2.shape[0], v2.shape[1]))
        for i in range(v5.shape[0]):
            for j in range(v5.shape[1]):
                temp = 1 + (i * v5[i,j]) * ((v6[i,j] - v4) / v3)
                v6[i,j] = v8
                v2[i,j] = v10
        return v6


# Initializing the model
m = Model()

