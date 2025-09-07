
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.permute(x1, 0, 2) # Permute the first tensor
        v2 = torch.permute(x2, 1, 0) # Permute the second tensor
        v3 = torch.bmm(v1, v2).squeeze(-1) 
        return v3

m  = Model()

