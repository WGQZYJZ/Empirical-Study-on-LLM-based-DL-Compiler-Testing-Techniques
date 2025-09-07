
class Model(torch.nn.Module):
    def __init__(self, num_output=1):
        super().__init__()
        self.num_output = num_output

        # Input of this layer is always reshaped tensor.
        self.linear  = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        t1 = v1.view(-1, self.num_output, -1)
        t2 = torch.relu(t1)

        return t2


# Initializing the model
m = Model()


