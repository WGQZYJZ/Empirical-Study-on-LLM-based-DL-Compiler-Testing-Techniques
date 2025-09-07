
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = torch.nn.Conv2d(3, 8, 1) # Conv layer with kernel size 1 and stride 1
        self.layer2 = torch.nn.Conv2d(8, 8, 1)

    def forward(self, x):
        output  = x  # Forward the input tensor
        output  = self.layer1(output) # Run the conv layer on the output
        output  = F.relu(output)
        output  = self.layer2(output)
        return output


# Initializing the model
m  = Model()

