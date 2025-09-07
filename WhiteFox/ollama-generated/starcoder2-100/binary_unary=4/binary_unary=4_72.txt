
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1) + self._other
        v2 = torch.relu(v1)
        return v2

    @staticmethod
    def _get_other():
         return torch.randn() * 0.5

 # Initializing the model
m = Model()

 # Inputs to the model 
 x1 = torch.randn(1, 3, 64, 64)
 
 # Keyword arguments passed for model.forward(x1):
 _other = m._get_other()
 
# __output__ is the return value of model.forward(x1), which is equal to m(x1)

