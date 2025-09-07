
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(2, 4)
        self.linear2 = torch.nn.Linear(4, 2)

    def forward(self, x):
        v1 = torch.cat([x, x], dim=0) # Concatenate tensor x twice along dimension 0.
        v2 = v1.view(-1, 8) # Reshape the concatenated tensor into a (num_examples, ) vector.
        return torch.relu(torch.nn.functional.linear(v2, self.linear1.weight, self.linear1.bias)) + torch.sigmoid(torch.nn.functional.linear(v2, self.linear2.weight, self.linear2.bias))

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(8)
