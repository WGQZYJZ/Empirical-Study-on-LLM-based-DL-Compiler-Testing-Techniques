
class Model(torch.nn.Module):
    def __init__(self, x1, x2, x3, x4, x5):
        super().__init__()
        self.linear1 = torch.nn.Linear(...)  # Concatenate all tensors and permute to input (2, 2)
        self.linear2 = torch.nn.Linear(...)
        self.linear3 = torch.nn.Linear(...)
        self.linear4 = torch.nn.Linear(...)
        self.linear5 = torch.nn.Linear(...)

    def forward(self):
        x1 = self.linear1(x1)  # Permute all tensors
        x2 = self.linear2(x2)
        x3 = self.linear3(x3)
        x4 = self.linear4(x4)
        x5 = self.linear5(x5)
        return torch.relu(...)


# Inputs to the model
x1, x2, x3, x4, x5  = ...  # Initialize the tensors as in your model
