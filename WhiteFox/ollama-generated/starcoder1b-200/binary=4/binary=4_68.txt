
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(in_features=64, out_features=10)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 2 # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model
m = Model()


