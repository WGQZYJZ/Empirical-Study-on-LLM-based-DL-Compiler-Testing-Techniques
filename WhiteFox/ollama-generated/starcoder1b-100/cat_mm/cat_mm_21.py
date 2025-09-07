
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=1)
        self.dim   = dim
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2).view(-1, self.dim, 4, 4) # Reshape the input tensor to flatten it into a 2D matrix
        v2 = torch.cat([v1, v1, ..., v1]) # Concatenate the result tensors along the last axis
        return torch.cat([self.conv1(x1), self.conv2(v2)], dim=-1)


# Initializing the model
m = Model()

