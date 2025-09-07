
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 10)

    def forward(self, x):
        t1 = torch.cat([x, x], dim=1) # Concatenate input with itself along the dimension 1 (i.e., the last axis). The generated tensor has dimension 4.
        t2 = t1.view(-1, 20)  # Reshape the concatenated tensor into a tensor of dimension 3 with dimension values 8 and -1 (i.e., dynamic size for each axis).
        t3 = torch.relu(t2)  # Apply ReLU operation to the reshaped tensor.

        return t3


# Inputs to the model
x1 = torch.randn(4, 2, 2)
