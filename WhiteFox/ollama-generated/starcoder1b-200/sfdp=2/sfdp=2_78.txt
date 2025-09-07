
class Model(torch.nn.Module):
    def __init__(self, embedding_dim: int, hidden_dim: int):
        super().__init__()
        self.embedding_dim = embedding_dim
        self.hidden_dim = hidden_dim

        self.linear1 = torch.nn.Linear(embedding_dim, hidden_dim)  # Linear layer 1
        self.linear2 = torch.nn.Linear(hidden_dim, embedding_dim)  # Linear layer 2

    def forward(self, x):
        x = self.linear1(x)
        x = torch.sigmoid(self.linear2(x))  # Sigmoid function
        return x


# Initializing the model
m = Model(embedding_dim=64, hidden_dim=50)


# Inputs to the model
key = torch.randn(3, 10, 50, requires_grad=True)
query = torch.randn(1, 3, 10, 50)  # We should specify `requires_grad=False` if you do not want to record the gradients for `self.linear2`.
