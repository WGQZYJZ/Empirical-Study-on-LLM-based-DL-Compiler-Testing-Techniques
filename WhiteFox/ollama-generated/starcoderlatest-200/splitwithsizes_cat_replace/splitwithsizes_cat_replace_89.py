
class Model(torch.nn.Module):
    def __init__(self, input_dim = 8):
        super().__init__()
 
    def forward(self, x1):
        split_tensors = torch.split(x1, self.input_dim, dim=1)
        concatenated_tensor = torch.cat(split_tensors)
        return concatenated_tensor
 
 # Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
