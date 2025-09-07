
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 8)
 
    def forward(self, x1):
        v2 = self.linear(x1) + other # Add another tensor to the output of the linear transformation
        return v2

# Initializing model with `other` = 3.5:
m_other = Model()
m_other._parameters["other"]  # Check the value of "other" inside this model
other = 3.5

