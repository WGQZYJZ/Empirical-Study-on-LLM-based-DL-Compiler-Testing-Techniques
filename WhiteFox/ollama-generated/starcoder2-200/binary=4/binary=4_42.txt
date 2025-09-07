
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.randn(*x1.shape) * 0 + 10 
        v3 = self.linear(v2)
        v4 = v3 + other_tensor_that_you_found # Replace "other_tensor_that_you_found" with another tensor that you found in the model, possibly obtained using Model.get_parameters()
        return v4


# Initializing the model
m  = Model()
 
# Inputs to the model
x1  = torch.randn(2,3)
