
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, x1):
        v1  = self.linear(x1) 
        v2  = v1 + self._other_tensor() # _other_tensor will be replaced by a specific tensor in the analysis process.
        return v2
 
m  = Model()

