
class Model(torch.nn.Module):
    def __init__(self, dim=2):
        super().__init__()
        self.fc1 = torch.nn.Linear(100, 3)
        self.fc2 = torch.nn.Linear(100, 8)
        self.fc3 = torch.nn.Linear(3, dim)
 
    def forward(self, x):
        # Concatenate two inputs along a specified dimension
        out1 = torch.cat([x, x], dim=dim)
        
        # Perform the following matrix multiplication to add the two tensors
        t1  = self.fc1(out1)
        t2  = self.fc2(t1)
        t3  = torch.exp(-t2)
        t4  = torch.sqrt(t3 + 1)
        t5  = t4 * (self.fc3(out1))
        
        return t5


# Initializing the model
m = Model()

