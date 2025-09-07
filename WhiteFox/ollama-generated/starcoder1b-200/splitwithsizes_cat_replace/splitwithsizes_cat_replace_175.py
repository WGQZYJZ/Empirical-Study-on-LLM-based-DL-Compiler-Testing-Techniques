
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        split_tensor0 = torch.split(x1, [2], dim=0)[0]
        concatenated_tensor0 = torch.cat([
            split_tensor0[i] for i in range(len(split_tensor0))
        ], dim=0)

        split_tensor1 = torch.split(concatenated_tensor0, [3], dim=1)[0]
        concatenated_tensor1 = torch.cat([
            split_tensor1[i] for i in range(len(split_tensor1))
        ], dim=1)

        v1  = self.conv(x1) * 0.5
        v2  = v1 * 0.7071067811865476
        v3  = torch.erf(v2)
        v4  = v3 + 1
        v5  = v1 * v4
        v6 = v5 + 1
        return v6


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
