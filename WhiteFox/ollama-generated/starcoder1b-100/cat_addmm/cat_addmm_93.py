
class Model(torch.nn.Module):
    def __init__(self, input_shape):
        super().__init__()
        self.input_shape = tuple(input_shape)
        self.fc1 = torch.nn.Linear(self.input_shape[0], 32, bias=False)
        self.fc2 = torch.nn.Linear(self.input_shape[1], 32, bias=False)
        self.fc3 = torch.nn.Linear(4 * 5 * 8, 64, bias=True)

    def forward(self, x):
        m1 = torch.randn(x.size()[0], self.input_shape[1])
        m2 = torch.randn(x.size()[0], self.input_shape[0])
        m3 = torch.cat([m1, m2], dim=1)  # Add two matrices together along the second axis of input
        m4 = self.fc1(m3)
        m5 = self.fc2(m4)
        m6 = m5 + 1  # Add 1 to the output of each node
        m7 = m6 * m1  # Multiply the output by each of the nodes in a batch
        return torch.cat([m7, x], dim=1)


# Initializing the model
m = Model(tuple([32, 8]))

