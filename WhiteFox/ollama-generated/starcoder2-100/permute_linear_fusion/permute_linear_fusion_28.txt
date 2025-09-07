
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.tensor([[2]]) # this line is an insertion
        return v1 * 4

