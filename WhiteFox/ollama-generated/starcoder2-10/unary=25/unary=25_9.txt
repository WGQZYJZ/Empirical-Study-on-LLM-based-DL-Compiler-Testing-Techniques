
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(256, 1)

    def forward(self, x1):
        v1  = self.linear(x1)

        # Your code: Create the boolean tensor v2 that has a True value for each element in v1 if the corresponding element in v1 is greater than 0 and False otherwise
        v2 = ???

        # Your code: Create the new output of t3 by multiplying the linear transformation to negative_slope (an input parameter of this activation function)
        v3 = ????
        
        # Your code: For each element in v2, if True then choose corresponding element from v1 else chosen from t3. 
        v4  = torch.where(v2, v1, v3)

        return v4

# Initializing the model with a parameter for LeakyReLU activation function
negative_slope  =0.5
m = Model()

 # Inputs to the model
 x1  = torch.randn(64, 256)
 __output__  = m(x1)
 