
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(10, 2)
        self.relu    = torch.nn.ReLU()
        self.linear2 = torch.nn.Linear(2, 5)
 
    def forward(self, x):
        out  = self.linear1(x) + 1.5  # Input is the value of '1' and a plus sign ('+'), so here the output of the first layer should be the same as input
        out2 = self.relu(out)      # Apply relu to the result of the previous layer
        out3 = self.linear2(out2) + 5  # Input is the value of '5' and a plus sign ('+'), so here the output of the second layer should be the same as input
        return out3


# Initializing the model
m = Model()


