
class Model(torch.nn.Module):
    def __init__(self, num_splits=2):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.split_tensors = []
        for i in range(num_splits):
            tensor = torch.randn(1, 3, 64, 64)
            self.split_tensors.append(tensor)
 
    def forward(self, x1):
        assert len(x1.size()) == 4
        v1 = torch.cat(list(map(lambda t: self.conv(t), self.split_tensors)), dim=-1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
