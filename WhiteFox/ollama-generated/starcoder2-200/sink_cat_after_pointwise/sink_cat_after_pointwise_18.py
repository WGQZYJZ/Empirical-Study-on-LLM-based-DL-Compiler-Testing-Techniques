
class Model(torch.nn.Module):
    def __init__(self, x1_dim=256, x2_dim=100, x3_dim=48):
        super().__init__()
        self.linear = torch.nn.Linear(x1_dim + x2_dim + x3_dim, 1)

    def forward(self, x1, x2):
        v1 = x1.reshape(-1, 1).permute(0, 2, 1) # (N, 1, D)
        v2 = torch.cat([v1, x2], dim=2) #(N*D, C+D, 1)
        v3 = self.linear(torch.relu(v2)) # (N*D, 1)
        return torch.nn.functional.softmax(v3).view(-1)


# Initializing the model and generating inputs to the model:
m = Model()
x1_dim, x2_dim, x3_dim  = [random.randint(500, 756), random.randint(48, 50)]
x1 = torch.rand((4,) + (x1_dim,))
x2 = torch.rand((4,) + (x1_dim - x3_dim,) + (x3_dim,))
