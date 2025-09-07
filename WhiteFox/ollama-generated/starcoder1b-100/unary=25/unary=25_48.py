
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
 
    def forward(self, x1):
        v1 = self.linear(x1) > 0  # Create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0, and False otherwise
        v2 = torch.where(v1, x1, -1 * (self.linear(x1)))  # For each element in t2, if the element is True, choose the corresponding element from t1, otherwise choose the corresponding element from t3
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(2, 3)
