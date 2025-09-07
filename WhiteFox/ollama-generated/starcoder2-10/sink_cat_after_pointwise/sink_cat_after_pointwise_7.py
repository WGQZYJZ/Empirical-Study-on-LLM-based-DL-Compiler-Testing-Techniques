
class Model(torch.nn.Module):
    def __init__(self, k1, k2):
        super().__init__()
        self.weight1  = torch.nn.Parameter(torch.rand([k1]))
        self.weight2  = torch.nn.Parameter(torch.rand([k1]))

    def forward(self, x1):
        v1  = torch.relu(x1 @ self.weight1)
        v2  = torch.cat((v1 + x1.permute(0, 2, 1),
                         torch.nn.functional.linear(v1.permute(0, 2, 1),
                                                    self.weight2)),
                        dim=1).view(-1, k1)
        return v2

# Initializing the model
m = Model(3, 5)

