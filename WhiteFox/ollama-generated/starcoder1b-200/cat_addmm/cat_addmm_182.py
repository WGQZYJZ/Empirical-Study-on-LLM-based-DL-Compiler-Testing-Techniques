
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, 1)
        self.conv2 = torch.nn.Conv2d(4, 8, 1)
 
    def forward(self, x):
        x = F.elu(x + x.mean(dim=0)) # Perform ELU activation to the input tensor
        x1 = self.conv1(x)
        x2 = self.conv2(x)
        y = torch.cat([x1, x2], dim=1)  # Concatenate the two inputs along the third dimension
        return y


# Initializing the model
m = Model()


