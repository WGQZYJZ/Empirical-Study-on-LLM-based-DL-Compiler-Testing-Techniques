
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256, 3072)
        self.linear2 = torch.nn.Linear(3072, 10)
 
    def forward(self, x1, x2):
        z = F.relu(self.linear1(x1))  # Apply ReLU to the first layer of the network
        z = self.linear2(z)        # Apply the second linear layer of the network on top of the ReLU output
        return z


# Initializing the model
m  = Model()


