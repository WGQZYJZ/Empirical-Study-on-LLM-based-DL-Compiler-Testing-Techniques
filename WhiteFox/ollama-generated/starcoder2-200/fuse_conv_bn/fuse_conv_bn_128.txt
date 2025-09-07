
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 16, kernel_size=(5, 7))

    def forward(self, x):
        v1  = x.permute(0, 3, 1, 2) # Permute the input tensor to match the ConvXd pattern
        v2  = torch.nn.functional.conv2d(v1, self.conv.weight, bias=None) 
        v3  = torch.nn.functional.batch_norm(v2)
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(16, 3, 50, 47).to('cuda')
__output__  = m(x1)


