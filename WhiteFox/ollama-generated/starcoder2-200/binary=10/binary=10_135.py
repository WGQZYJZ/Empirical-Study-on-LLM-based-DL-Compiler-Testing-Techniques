
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1) + self.__output__ # Here, the input tensor is x1 and output of linear transformation (from the previous model) is __output__.
        return v1


# Initializing a model for each of the scenarios specified by the pattern 
m_p0 = Model()
 
x1 = torch.randn(32, 32) # Input tensor for model m_p0
__output__  = m_p0(x1).sum().numpy() # Output of linear transformation from previous model is passed as input to m_p0.
 
