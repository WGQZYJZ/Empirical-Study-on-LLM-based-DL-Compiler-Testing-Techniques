
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v2 = torch.bmm(x1.permute(0, 2, 1), y1) # or torch.matmul(x1.permute(0, 2, 1), y1) for bmm or torch.matmul(y1.permute(0, 2, 1), x1) for matmul
        v3 = torch.bmm(v2, v2) # or torch.matmul(v2, v2) for bmm or torch.matmul(v2, v2) for matmul
        return v3

# Initializing the model
m  = Model()


