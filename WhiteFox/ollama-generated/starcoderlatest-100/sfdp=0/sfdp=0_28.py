
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.scaled_dot_product = torch.nn.Linear(768, 768)
 
    def forward(self, x1):
        v1 = self.scaled_dot_product(x1)
        return v1


# Inputs to the model
query  = torch.randn(1, 768)
key  = torch.randn(1, 768)
