
class Model(torch.nn.Module):
    def __init__(self, hidden_size):
        super().__init__()
        self.conv = torch.nn.Linear(2048, 512)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, x2, x2.T)  # Perform a matrix multiplication of x1 and x1 transpose and add it to the input
        return torch.cat([v2], dim=0)


# Initializing the model
m = Model()


