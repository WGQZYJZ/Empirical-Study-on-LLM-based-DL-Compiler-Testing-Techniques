
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.split(x1[0], [32, 64], dim=2) 
        v2  = torch.cat([v1[i] for i in range(len(list(map(int, [32, 64]))))], dim=2)
        return x1


# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = (torch.randn(50, 8, 3, 7), torch.randn(1, 3, 64, 64)) # First element in this tuple is the input tensor and second element is another input tensor with size 1 x 3 x 64 x 64
 
