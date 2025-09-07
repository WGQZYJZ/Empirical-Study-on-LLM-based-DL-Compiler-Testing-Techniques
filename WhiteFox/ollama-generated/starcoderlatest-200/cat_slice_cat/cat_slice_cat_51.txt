
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1 = torch.cat([x1] + [x2 for _ in range(3)], dim=1) # Concatenate input tensors along dimension 1
        return torch.cat(t1, dim=1)


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(3, 1024, device="cuda")
x2 = torch.randn(5, 1024, device="cuda")
