
class Model(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.dim = dim
        self.fc1 = torch.nn.Linear(4, 5)
 
    def forward(self, x, hidden, memory, key_mask, value_mask, position_mask):
        v = self.fc1(torch.cat([x, hidden], dim=-1))
        return output


# Initializing the model
m = Model(8)


# Inputs to the model
x  = torch.randn(2, 4, 64, 64)
hidden  = torch.randn(2, 5)
memory = torch.randn(2, 5, 128, 128)
key_mask  = torch.zeros((2, 64))
value_mask = torch.zeros((2, 64))
position_mask = torch.zeros((2, 30, 1)).type(torch.long)


