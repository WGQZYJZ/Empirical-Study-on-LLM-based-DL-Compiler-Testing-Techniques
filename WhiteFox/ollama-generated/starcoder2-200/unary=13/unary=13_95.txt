
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(128 * 3, 5)
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.sigmoid(v1)
        v3  = v1  * v2
        return v3


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 128 * 3).cuda()


# Executing the model in inference mode.
# In this example, we are using CUDA (GPU) backend with batch size of 16. Hence, we need to pass the argument .cuda() at the end of the input tensor.
__output__  = m(x1).cpu()

