
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t2 = torch.nn.functional.linear(x1, self.linear.weight, self.linear.bias) # Apply linear transformation to the input tensor.
        return torch.nn.functional.dropout(t2, 0.5) # Apply dropout with probability of 0.5


m  = Model()


__output__  = m(torch.randn(10)) 
