
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = torch.nn.Linear(490007654, 10, bias=True)
 
    def forward(self, x):
        v1  = self.conv (x) 
        v2  = v1 - other # Subtract a tensor or scalar "other" from the output of the convolution. It may be a constant number or a tensor with the same size as `v`.
        v3  = torch.relu(v2, inplace=False) # Apply the ReLU (Rectified Linear Unit) activation function to the result
        return v3
# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(64, 8 ,30 ,50)
other  = torch.Tensor([7.])
__output__   = m(x1)


