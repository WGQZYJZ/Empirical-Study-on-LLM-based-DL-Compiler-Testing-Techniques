
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(5, 4)

    def forward(self, x):
        y0 = self.linear1(x).to(dtype=torch.float32)
        y1 = y0 - other # subtract 'other' from the output of the linear transformation
        y2 = torch.relu(y1 + 5) # Apply the ReLU activation function to the result

        return y2

# Initializing the model
m = Model()
