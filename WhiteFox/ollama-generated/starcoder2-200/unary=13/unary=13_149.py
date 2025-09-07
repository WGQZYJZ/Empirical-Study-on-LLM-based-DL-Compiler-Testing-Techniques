
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(512 * 4, 10)
 
    def forward(self, x1):
        v1 = self.linear(x1).reshape(-1, 8, 6)
        v3 = v1[:, :, :] * v1[:, 4, :]
        return v3


# Initializing the model