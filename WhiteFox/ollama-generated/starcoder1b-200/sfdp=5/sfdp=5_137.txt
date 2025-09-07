
class Model(torch.nn.Module):
    def __init__(self, hidden_size: int):
        super().__init__()
        self.fc = torch.nn.Linear(hidden_size, 10)
 
    def forward(self, x1: torch.Tensor):
        # x1: [batch_size, 64, 64]
        batch_size = x1.shape[0]
        h  = self.fc(x1).view(-1, batch_size)
        return h


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
