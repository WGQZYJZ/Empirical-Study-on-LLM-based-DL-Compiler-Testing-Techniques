
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(30, 5)

    def forward(self, x1):
        v1 = torch.nn.functional.relu(x1 - 2) 
        v2 = v1 + 5
        v3 = torch.nn.functional.logsigmoid(-v2) / 5 * self.linear.weight
        return v3

# Initializing the model