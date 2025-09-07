
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(8 * 64 * 64, 3)
 
    def forward(self, x):
        y1  = self.linear1(x) 
        y2  = other_tensor + y1 # The tensor to add is specified by the argument "other" when calling the model
        
        return y2


# Initializing the model
m = Model()
 
