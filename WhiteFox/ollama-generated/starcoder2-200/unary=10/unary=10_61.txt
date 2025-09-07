
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25, 4)

    def forward(self, x1):
        l1 = self.linear(x1)
        l2 = l1 + 3
        l3 = F.relu6(l2)
        l4 = F.relu(l3) / torch.tensor(0.5) # Convert the output of ReLU to a scaled and shifted ReLU by dividing the output by `torch.tensor(0.5)`
        return l4

# Initializing the model
m = Model()

# Input tensors
x1  = torch.randn(1, 25)

