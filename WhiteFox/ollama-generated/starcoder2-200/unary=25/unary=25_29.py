
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8 * 16, 32)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 > 0 # create a boolean tensor where each element is True if the corresponding element in t1 is greater than 0 and False otherwise
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3) # for each element in t2, choose the corresponding element from t1 if the element is True, otherwise choose the corresponding element from t3
        return v4

# Initializing model 
m = Model()
negative_slope = float(-0.598767152957248) # random.uniform(-3, -2), the input negative slope is randomly selected within [-3, -2]

# Inputs to the model
x1  = torch.randn(1, 8 * 16)
__output__= m(x1)

