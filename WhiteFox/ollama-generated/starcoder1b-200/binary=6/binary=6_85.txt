
class Model(torch.nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)
 
    def forward(self, x):
        return self.linear(x) - 1


# Initializing the model
m = Model(10)


