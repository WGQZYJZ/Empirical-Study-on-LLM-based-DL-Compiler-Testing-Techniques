

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v3 = torch.bmm(x1, self.linear)  # or torch.matmul(x1, self.linear)
        return v3

# Initializing the model