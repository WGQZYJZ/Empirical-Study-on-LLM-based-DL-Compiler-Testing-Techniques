
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y1):
        v1  = torch.permute(x1, 0, 2, 1) # Permute the input tensor A with 3D shape (2, 4, 5).
        v2 = torch.permute(y1, 0, 2, 1) # Permute the input tensor B with 3D shape (2, 7, 8) or (2, 8, 7).
        v3  = torch.bmm(v1, v2)
        return v3

m = Model()


# Initializing the model