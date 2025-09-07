
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1, self.linear.weight)  # Linear transformation
        v2 = v1.permute(-1, -3, -2) # Permute the output tensor of the linear function
        return v2

# Initializing the model
m = Model()

