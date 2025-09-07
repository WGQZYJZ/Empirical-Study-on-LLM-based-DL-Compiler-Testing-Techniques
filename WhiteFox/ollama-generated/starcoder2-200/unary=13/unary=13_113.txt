
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8 * 64 * 64, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = F.sigmoid(v1)
        v3  = v1  * v2
        return v3


# Initializing the model and setting the device to GPU (if available). This can be skipped if not using GPU.
m  = Model()
if torch.cuda.is_available():
    m = m.to(torch.device('cuda:0'))
    
# Inputs to the model
x1  = torch.randn(8, 64 * 64).reshape(-1, 8 * 64 * 64)

 # Convert the inputs into tensors on GPU (if available), and run the model with these tensors. This can be skipped if not using GPU.
if torch.cuda.is_available():
    x1 = x1.to(torch.device('cuda:0'))
    yh  = m(x1)

