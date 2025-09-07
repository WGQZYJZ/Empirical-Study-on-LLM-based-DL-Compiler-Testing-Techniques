
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other # This should be a new tensor of the same shape as x1 (from previous model) that will be added to the output of conv in this model.
        return torch.relu(v1)


# Initializing the model
m = Model()
__output__  = m(x1)

