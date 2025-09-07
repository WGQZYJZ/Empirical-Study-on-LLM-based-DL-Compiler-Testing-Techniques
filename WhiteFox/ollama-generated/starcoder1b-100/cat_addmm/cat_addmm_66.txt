
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(20, 5)
        self.fc2 = torch.nn.Linear(5, 5)
 
    def forward(self, x1, x2):
        # Concatenate the input tensors along a specified dimension
        t1 = torch.cat([x1, x2], dim=0)
        # Pass the concatenated tensor through two linear layers to get two features of the same size
        f1  = self.fc1(t1)
        f2  = self.fc2(f1)
        return f2


# Initializing the model
m = Model()

