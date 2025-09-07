
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2048, 512)
        self.linear2 = torch.nn.Linear(512, 512)
 
    def forward(self, x1, other=None):
        x1 = x1.view(-1, 784) # Flatten the input tensor (the data is stored as a 1-dimensional vector).
        x1 = F.relu(self.linear1(x1))
        x2 = self.linear2(x1)
        if other is not None:
            x3 = x2 + other
            return torch.sigmoid(x3)
        else:
            return torch.sigmoid(x2)


# Initializing the model
m = Model()
other = 10 * torch.ones(1, 512) # Add another tensor to the output of the linear transformation
