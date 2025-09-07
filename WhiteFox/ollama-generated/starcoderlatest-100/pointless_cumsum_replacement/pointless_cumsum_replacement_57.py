
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.tensor = torch.full([8], 1, dtype=torch.int32)
 
    def forward(self, x1):
        v1 = torch.cumsum(x1, 1) # Compute the cumulative sum of the elements of the tensor along dimension 1
        return v1

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(8, 64, 64, dtype=torch.int32, layout=torch.strided, device="cuda", pin_memory=True)
