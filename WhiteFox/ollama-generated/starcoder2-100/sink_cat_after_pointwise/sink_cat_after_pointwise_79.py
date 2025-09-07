class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        t1  = torch.cat([x1, x2], dim=0)
        t3  = torch.relu(t1.view(-1).sum()) # This is a sink point-wise operation
        return t3
