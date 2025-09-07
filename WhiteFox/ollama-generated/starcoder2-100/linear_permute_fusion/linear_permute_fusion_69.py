
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(100, 50)

    def forward(self, x1):
        v2  = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias).permute(-1,-3,-4,-2)

        return v2

# Initializing the model
m  = Model()


# Inputs to the model