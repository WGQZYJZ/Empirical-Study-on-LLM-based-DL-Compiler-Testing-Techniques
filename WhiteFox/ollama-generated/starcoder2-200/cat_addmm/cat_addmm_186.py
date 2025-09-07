
class Model(torch.nn.Module):
    def __init__(self, dim=256):
        super().__init__()
        self.fc  = torch.nn.Linear(10 * 37 * 4, dim)
        self.bn  = torch.nn.BatchNorm1d(dim)

    def forward(self, x1):
        v1  = x1[:, :, None].repeat_interleave([1], axis=2).reshape(-1, 10 * 37 * 4)
        v2  = self.fc(v1)
        v3  = torch.addmm(v2[:, :5*8**2], self.mat1, self.mat2) 
        v4  = torch.cat([v3 + 1], dim=1) # output of cat operation
        return v4

m  = Model()

