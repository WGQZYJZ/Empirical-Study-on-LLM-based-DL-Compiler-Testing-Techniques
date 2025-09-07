
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x0, y0, x1, y1):
        v2 = torch.cat([x0[:, 5:y0], x1[3:7]], dim=1)
        return v2

# Initializing the model
m  = Model()

 # Inputs to the model
x0  = torch.randn(4, 9223372036854775807)
y0  = x0[:, 5:10].shape[1]
x1  = torch.randn(4, 3)

 # Generating an example of input tensor to the model m
