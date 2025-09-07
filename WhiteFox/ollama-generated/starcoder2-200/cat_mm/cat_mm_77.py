
class Model(torch.nn.Module):
    def __init__(self, l1=256):
        super().__init__()
 
        # Define layer 1, linear layer with `in_features` as length of `l1` and `out_features` = size of `l1`
        self.lin1 = torch.nn.Linear(l1, len(l1))
 
    def forward(self, input1):
        return torch.cat([self.lin1(input1), ...])
# Initializing the model
m  = Model()


# Inputs to the model (size: `torch.Size([32, 256])`)
x1 = torch.randn(32, 256)
__output__  = m(x1).shape
