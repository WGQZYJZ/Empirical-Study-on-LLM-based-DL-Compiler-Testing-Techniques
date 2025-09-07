
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v40  = conv(v1)
        v50  = torch.relu(v40)

        return v50


# Initializing the model
m  = Model()


# Inputs to the model
__input_t1  = torch.randn(3, 8, 672//2 + 5, 192//2 + 5 ) # You are required to provide input_tensor t1 for the first time.
__input_t40  = torch.randn(v40.shape) # You are required to provide input_tensor t38 of the same shape with t40 in forward() 
__input_v50   = torch.relu(conv(__input_t1))

x1  = torch.randn(1, 3, 64, 64) # You are required to provide input for forward() of Model()

