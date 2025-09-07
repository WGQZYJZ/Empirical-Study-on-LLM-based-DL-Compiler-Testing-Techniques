
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.permute(x1, 0, 2) 
        v2 = torch.bmm(v1, torch.permute(x2, 0, 2)) # or torch.matmul(v1, torch.permute(x2, 0, 2))
        return v2

# Initializing the model
m = Model()

