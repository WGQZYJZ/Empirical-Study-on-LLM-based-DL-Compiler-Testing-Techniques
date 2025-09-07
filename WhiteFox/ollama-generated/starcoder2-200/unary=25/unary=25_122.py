
class Model(torch.nn.Module):
    def __init__(self, negative_slope = 0.5):
        super().__init__()
        self.linear = torch.nn.Linear(128 * 32 ** 2 , 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) 
        v2 = (v1 > 0).float() # Boolean Tensor
        v3 = v1 * negative_slope # Multiplication
        v4 = torch.where(v2, v1, v3 )# Where each element is True the corresponding element from t1, otherwise the corresponding element from t3
        return v4

# Initializing model
m  = Model()
negative_slope = 0.5 # The negative slope used in the leaky ReLU activation function

