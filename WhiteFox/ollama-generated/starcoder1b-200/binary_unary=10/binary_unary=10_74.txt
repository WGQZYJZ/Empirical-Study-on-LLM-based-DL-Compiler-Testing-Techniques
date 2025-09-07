
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1) + 2
        return v1


# Inputs to the model
input_tensor = ...  # A valid input tensor of shape (batch size, num features)
