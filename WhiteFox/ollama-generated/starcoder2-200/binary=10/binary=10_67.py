
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(48, 20)
 
    def forward(self, x1, x2):
        v1  = self.linear(x1) 
        v3  = other_tensor + v1 # Adding another tensor to the output of a linear transformation
        return v3

# Initializing the model