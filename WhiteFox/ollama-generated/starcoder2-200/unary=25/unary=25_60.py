
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64, 25)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0 
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) # For each element in the boolean tensor created earlier, if it is True, choose the corresponding element from t1; otherwise choose the corresponding element from t3
        return v4

# Initializing the model
m  = Model()
__output__  = m(x1)

