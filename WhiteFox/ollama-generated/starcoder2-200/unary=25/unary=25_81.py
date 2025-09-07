
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) # apply a linear transformation to the input tensor 
        v2 = v1 > 0 # create a boolean tensor where each element is True if its corresponding element in t1 is greater than zero and False otherwise
        v3 = negative_slope = torch.tensor(-0.5, dtype=torch.float32)
        v4 = v1 * v3 
        v5 = torch.where(v2, v1, v3) # for each element in the boolean tensor, if its corresponding element is True, choose from t1 or t3; otherwise select from t1
        return v5

# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(20) # create a 4 dimensional tensor where each element is sampled uniformly from the range [0, 63]
