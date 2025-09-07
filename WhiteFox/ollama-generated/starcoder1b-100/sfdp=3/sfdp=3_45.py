
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(d_v, 8)
        self.fc2 = torch.nn.Linear(8, d_k)

    def forward(self, v):
        f1 = self.fc1(v)  # Input vector
        f2 = f1.unsqueeze(-1).matmul(self.fc2.weight)  # Dot product of the input vector and the weight tensor
        return torch.nn.functional.softmax(f2, dim=-1)  # Apply softmax to the output


# Initializing the model
m = Model()


# Inputs to the model
v = torch.randn(d_v)
