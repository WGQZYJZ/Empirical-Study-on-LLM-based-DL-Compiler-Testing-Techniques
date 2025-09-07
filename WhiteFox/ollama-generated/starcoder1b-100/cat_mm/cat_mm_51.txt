
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = [v1]*4 # Concatenation of the output tensors along the third dimension
        t2 = torch.cat(t1, dim=1)  # Concatenation of each result tensor along a new dimension
        return t2


# Initializing the model
m = Model()

