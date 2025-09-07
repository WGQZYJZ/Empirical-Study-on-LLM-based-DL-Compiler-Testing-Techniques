
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1  = torch.nn.Linear(256, 8)
        self.linear2  = torch.nn.Linear(3904, 256)
        self.linear3  = torch.nn.Linear(73728, 134217728)
 
    def forward(self, x): 
        t1 = torch.mm(x, self.linear1.weight.data.clone()) # Applying multiplication between input and weight
        t2 = torch.mm(t1, self.linear2.weight.data.clone()) # Applying multiplication between the results of a multiplication between input and weight to the results of another multiplication between them to the weight 
        t3  = t2 + torch.mm(x, self.linear3.weight)
        return t3


# Initializing the model