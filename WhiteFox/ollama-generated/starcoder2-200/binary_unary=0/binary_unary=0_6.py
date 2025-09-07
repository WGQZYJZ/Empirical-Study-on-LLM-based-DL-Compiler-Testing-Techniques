
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other_tensor
        v3  = torch.relu(v2) 
        return v3

# Initializing the model with some tensors to be added in the above code as an input tensor (other). It is recommended that the tensors to be added should not be shared by all instances of this model.
m1, m2 = Model(), Model()
other  = torch.randn(3)

# Inputs to the models with the new input tensors. In the first instance x will have the value torch.randn(8, 64, 64).In the second instance x will be torch.randn(100, 52, 72), and then torch.randperm(5) would produce a random permutation of { 0..9 }.
__output_m1__, __output_m2__ = m1(x), m2(x)

