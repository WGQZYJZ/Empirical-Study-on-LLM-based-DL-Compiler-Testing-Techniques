
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        # Perform a linear transformation to the input tensor first
        v1 = torch.nn.functional.relu(input_tensor.permute(0, 2, 1))

        # Perform a recurrent transformation to generate a second transformed input
        v2 = self.linear.weight * torch.nn.functional.dropout(v1, self.p)

        # Re-run the forward pass with the second transformed input and obtain the output
        return v2


# Initializing the model
m = Model()
x1  = torch.randn(1, 2, 2)
