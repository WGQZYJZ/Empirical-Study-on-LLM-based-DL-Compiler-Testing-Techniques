
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        t1 = self.linear(x)
        t2 = (t1 > 0).type(torch.FloatTensor) # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        t3 = torch.where(t2, t1, t1 * self.negative_slope) # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return t3


# Initializing the model
m = Model()
