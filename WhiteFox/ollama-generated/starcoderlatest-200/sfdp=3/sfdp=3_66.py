
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8) 
        self.dropout1 = torch.nn.Dropout()
        self.linear2 = torch.nn.Linear(8, 16) 
        self.dropout2 = torch.nn.Dropout()
        self.linear3 = torch.nn.Linear(16, 32)
 
    def forward(self, x):
        v1 = self.linear1(x) # input_dim == input_tensor.size()[0]
        v2 = self.dropout1(v1)
        v3 = self.linear2(v2)
        v4 = self.dropout2(v3)
        v5 = self.linear3(v4)
        return v5


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
