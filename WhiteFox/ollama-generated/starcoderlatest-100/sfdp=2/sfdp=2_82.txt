
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 256)
        self.dropout = torch.nn.Dropout()
        self.linear2 = torch.nn.Linear(256, 8)
 
    def forward(self, x):
        v = self.dropout(torch.relu(self.linear1(x))) # Apply relu to the output of the linear layer and dropout to it 
        v  = self.linear2(v) 
        return v

# Initializing the model
m = Model()


