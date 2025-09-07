
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(32, 40)
 
    def forward(self, x):
        v1 = self.linear1(x) + other  # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model
m = Model()


