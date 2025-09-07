
class Model(torch.nn.Module):
    def __init__(self, conv1, bn1, conv2, bn2):
        super().__init__()
        self.conv1 = conv1
        self.bn1 = bn1
        self.conv2 = conv2
        self.bn2 = bn2

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.nn.functional.convXd(...) # X should match with ConvXd
        v3 = torch.nn.functional.batch_norm(...) # X can be 1, 2, or 3 representing the dimension
        v4 = self.bn1(v3)
        v5 = self.bn2(self.conv2(self.bn1(self.conv1(v4)))) # Fuse conv and batch norm layers into a single layer
        return v5


# Initializing the model
m  = Model(...) # X can be 1, 2, or 3 representing the dimension
