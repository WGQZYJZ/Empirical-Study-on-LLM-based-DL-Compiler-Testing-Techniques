
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.linear  = torch.nn.Linear(64*64*3, 1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).to(torch.float32) 
        v3  = v1 * -0.5 # Applying the Leaky ReLU, where each element in the output is multiplied by a negative slope (-0.5 in this case), and the boolean tensor is created with elements that are True if the corresponding element from t1 is greater than 0, and False otherwise
        v4 = torch.where(v2, v1, v3) # Applying the Leaky ReLU, where each element in the output is multiplied by a negative slope (-0.5 in this case), and the boolean tensor is created with elements that are True if the corresponding element from t1 is greater than 0, and False otherwise
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(32, 64*64*3)
__output__  = m(x1)


