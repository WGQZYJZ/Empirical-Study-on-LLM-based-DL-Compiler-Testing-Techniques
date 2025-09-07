
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2048, 512)
 
    def forward(self, x):
        v1 = self.linear(x) + other  # Add another tensor to the output of the linear transformation
        return v1


# Initializing the model
m = Model()


