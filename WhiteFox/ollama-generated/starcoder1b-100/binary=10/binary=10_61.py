
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(32, 64)
        self.add   = torch.nn.AddTensor()
 
    def forward(self, x1, *others):
        v1 = self.linear(x1) + self.add(*others)
        return v1


# Inputs to the model
input_tensor = ... # Generate input tensor for training
