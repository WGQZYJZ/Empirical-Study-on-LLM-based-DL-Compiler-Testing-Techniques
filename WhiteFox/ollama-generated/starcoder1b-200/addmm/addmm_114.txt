
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(10, 20)
 
    def forward(self, x1, inp=None):
        v1 = self.mm(x1) + inp  # Perform matrix multiplication on two input tensors and then add the result of this operation to another tensor 'inp'
        return v1


# Initializing the model
m = Model()


