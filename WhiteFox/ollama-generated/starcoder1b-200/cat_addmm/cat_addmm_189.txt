
class Model(torch.nn.Module):
    def __init__(self, hidden_size=8):
        super().__init__()
        self.linear1 = torch.nn.Linear(20, 5)
        self.linear2 = torch.nn.Linear(5, hidden_size)
        self.linear3 = torch.nn.Linear(hidden_size, 4)

    def forward(self, x):
        # Concatenate input and weight matrices together along the second axis
        x = torch.cat([x, torch.zeros((1, 10)).to(torch.float)], dim=1)
        # Perform linear layer operation with a hidden size of 8
        out = self.linear1(x)
        out = F.relu(out)
        # Reshape the output of linear layer into (20, 5) and perform another relu operation on the same
        out = torch.reshape(out, (-1, 5))
        out = self.linear2(out)
        # Reshape the output of linear layer into (20, hidden_size) and perform a final relu operation
        # followed by another reshaping operation to obtain a matrix with shape (20, hidden_size)
        out = torch.reshape(out, (-1, self.linear3(out).shape[1]))
        out = F.relu(self.linear3(out))
        # Reshape the output of linear layer into (20, 4) and perform a sigmoid operation to obtain
        # probabilities between 0 and 1 for each input
        out = torch.sigmoid(out)
        return out


# Initializing the model
m = Model()


