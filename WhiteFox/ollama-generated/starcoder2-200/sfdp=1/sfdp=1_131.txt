
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256, 30)
        self.linear2 = torch.nn.Linear(28*28 + 30, 30)
    
    def forward(self, x1):
        v1 = F.dropout(F.relu(self.linear1(x1)))
        v2 = torch.cat([v1, self._constant], dim=1).view(-1, 30*49 + 30) # Constant is a constant value 8
        return F.log_softmax(self.linear2(v2), dim=-1)

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.rand(6, 256)

# Outputs from the model
