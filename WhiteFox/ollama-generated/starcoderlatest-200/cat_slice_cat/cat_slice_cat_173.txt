
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.concat = torch.nn.Cat(dim=1)
 
    def forward(self, x1, x2):
        v1 = self.concat([x1, x2])
        return v1


# Inputs to the model
input_tensors = [torch.randn(5),
                  torch.randn(6)]
