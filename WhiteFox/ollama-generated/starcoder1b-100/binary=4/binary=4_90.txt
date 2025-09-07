
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.linear1 = torch.nn.Linear(8 * 7 * 7, 40)
        self.linear2 = torch.nn.Linear(40, 20)
 
    def forward(self, x1):
        x2 = self.conv1(x1)
        x3 = x2.view(x2.shape[0], -1) # flatten the tensor
        return self.linear1(x3), self.linear2(x3)
# Initializing the model
m  = Model()

