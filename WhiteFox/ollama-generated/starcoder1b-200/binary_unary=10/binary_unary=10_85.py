
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)

    def forward(self, x):
        y = self.linear(x) + torch.zeros(1, 16).to(x.device) # Use a linear transformation on the input tensor and then add another zero tensor to the result of the linear transformation
        return relu(y)


# Initializing the model
m = Model()


