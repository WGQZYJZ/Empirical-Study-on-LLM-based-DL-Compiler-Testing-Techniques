
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(5120, 8)
 
    def forward(self, x1):
        v1  = self.lin(x1)
        v2  = v1 + self.__output__.detach()  # Adding another tensor to the output of a linear transformation. The keyword argument "__output__" refers to the tensor created during the previous step in the inference.
        return v2

# Initializing the model
m  = Model()

