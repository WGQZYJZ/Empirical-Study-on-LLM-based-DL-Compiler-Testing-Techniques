
class Model(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.fc = torch.nn.Linear(input_dim, hidden_dim)

    def forward(self, x):
        x = F.relu(self.fc(x))
        return x


# Initializing the model
m = Model(3, 8)
m.weight.data.normal_()  # Set uniform random values to the weight tensor
m.bias.data.zero_()  # Set zeros to bias tensor

# Inputs to the model
x1 = torch.randn(1, 4096)
