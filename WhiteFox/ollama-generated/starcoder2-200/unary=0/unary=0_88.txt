
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1 ** 2
        v4  = v3 * v1 
        v5  = v4 * 0.044715
        v6  = v1 + v5
        v7  = v6 * 0.7978845608028654
        v8  = torch.tanh(v7) 
        v9  = v8 + 1
        v10  = v2 * v9  
        return v10

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 
 # Initializing a new model with different name and a new forward pass (a new function) that returns different values of v8 and v9 based on the value of v7
 m_new  = Model()
 
# Inputs to this new model (x2 is modified to include a new term that depends on the value of v7). 
# Since the original model’s v10 and this new model's v10 differ in terms of how they depend on other values, it is not allowed as an input for the model’s forward function. Instead, it will be considered as a novel input variable that is being created during runtime. 
 x2 = torch.randn(1, 3, 64, 64) * ((v7 <= 0).type(torch.FloatTensor))

# Evaluating the model’s output with x1 and the modified inputs (x2)
 __output__  = m(x1, x2)
