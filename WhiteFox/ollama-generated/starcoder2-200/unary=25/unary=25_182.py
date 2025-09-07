class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(256, 10)

    def forward(self, x): 
        v1 = self.linear(x)
        v2 = (v1 > 0).float() # Creating a boolean tensor where each element is True if the corresponding element in t1 is greater than 0 and False otherwise
        v3 = v1 * -2.5 # Multiplying the output of the linear transformation by the negative slope 
        v4 = torch.where(v2, v1, v3) # For each element in v2, if it's True then choose the corresponding element from t1 otherwise choose the corresponding element from 3
        return v4
