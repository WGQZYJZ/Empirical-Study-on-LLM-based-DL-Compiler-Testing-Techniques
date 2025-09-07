
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1  = x1.permute(0, 3) # Permute the input tensor A
        v2  = torch.bmm(v1, x2.permute(0, 2))
        return v2

# Initializing the model