
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.dropout = torch.nn.Dropout2d()

    def forward(self, x1):
        v1  = self.dropout(input_tensor)
        return v1

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 4, 5) 
 